from os import path
from base64 import b64encode as encode
import requests 
from json import loads
from json import dump as json_dump

class image_analysis :

    def __init__(self,api_key,image_path):

        if path.isfile(image_path):
            self.image_content=encode(open(image_path,'rb').read()).decode('UTF-8')
        else:
            raise FileNotFoundError('Image not found in given location')

        self.url = "https://vision.googleapis.com/v1/images:annotate?key="+api_key
        self.request_json={}
        self.image_path=image_path
        self.response={}
        self.best_description=None
        self.labels=None
        self.text_in_pic=None
        self.landmark_properties=None
        self.web_entities=[]
        self.get_results()
    
    def process_json(self):

        if 'webDetection' in self.response['responses'][0].keys():
            #self.web_entities=[(x['description'],x['score']*100) for x in self.response['responses'][0]['webDetection']['webEntities']]
            for i in self.response['responses'][0]['webDetection']['webEntities']:
                try:
                    self.web_entities.append((i['description'],i['score']))
                except KeyError :
                    pass
        if self.response['responses'][0]['webDetection']['bestGuessLabels']!={}:
            try:
                self.best_description=[x['label'] for x in self.response['responses'][0]['webDetection']['bestGuessLabels']]        
            except KeyError:
                pass

        if 'labelAnnotations' in self.response['responses'][0].keys():
        	self.labels=[(x['description'],x['score']*100) for x in self.response['responses'][0]['labelAnnotations']]
        
        if 'textAnnotations' in self.response['responses'][0].keys():
            try:
                self.text_in_pic=self.response['responses'][0]['textAnnotations'][0]['description']
            except KeyError:
                pass
        if 'landmarkAnnotations' in self.response['responses'][0].keys():
            try:
                self.landmark_properties=(self.response['responses'][0]['landmarkAnnotations'][0]['description'],self.response['responses'][0]['landmarkAnnotations'][0]['score'],self.response['responses'][0]['landmarkAnnotations'][0]['locations'][0]['latLng'])
            except KeyError :
                pass

    def get_results(self,no_of_lables=10):

        self.request_json = {"requests":[{"image":{"content":self.image_content},"features":[{"type":"LABEL_DETECTION","maxResults":no_of_lables},{"type":"LANDMARK_DETECTION","maxResults":no_of_lables},{"type":"LOGO_DETECTION","maxResults":no_of_lables},{"type":"TEXT_DETECTION"},{'type':'DOCUMENT_TEXT_DETECTION'},{"type":"WEB_DETECTION","maxResults":no_of_lables}]}]}
        self.response=loads(requests.post(self.url,data=str(self.request_json)).text.replace('  '," "))
'''
        with open('response.json','w') as file :
            json_dump(self.response,file,indent=4)
'''
        self.process_json()

    def labels_url(self):
    	return('https://www.google.com/search?q='+'+'.join([x[0] for x in self.labels])+'&t')

    def web_entities_url(self):
    	if self.web_entities==None:
    		raise RuntimeError('No web entities to generate url')
    	else:
    		return('https://www.google.com/search?q='+'+'.join([x[0] for x in self.web_entities])+'&t')

    def landmark_location_url(self):
    	if self.landmark_properties==None:
    		raise RuntimeError('No landmark details available to create url')
    	else:
    		return('https://www.google.com/maps/search/'+str(self.landmark_properties[2]['latitude'])+','+str(self.landmark_properties[2]['longitude'])+'/')

#======================================================================Main Document============================================================
'''
def cure(str):#This function is used to remove the single quoates which surround the image path (which gets formed during the drag and drop of the image in the terminal to get the image path)
    if '\'' in str :
        str=str.replace("'",'').strip()
    return(str)



image=image_analysis('AIzaSyBe7X9Q38FFfBPPff9gZ4Hto922OjTLHtk',cure(input('Enter the path of the file:')))
print('\n\n')


print('Lables=========>\n')
for i in image.labels:
    print(i[0],':',i[1],"% confidence")
print('\nWeb_Indentities========>\n')
for i in image.web_entities:
    print(i[0],':',i[1],'% confidence')
print('\nTextual Content==========>\n')
print((image.text_in_pic))
print('\nBest Description=========>\n')
print(image.best_description[0])
print('\nLandmark Detected=========>\n')
for i in image.landmark_properties:
	print(i)

input('\nPress enter to open label search')
from webbrowser import open as web_open
web_open(image.labels_url(),new=2)
input('\nPress enter to open web entity search')
web_open(image.web_entities_url(),new=2)
input('\nPress enter to open landmark location')
web_open(image.landmark_location_url(),new=2)
print('URL:',image.landmark_location_url())'''
