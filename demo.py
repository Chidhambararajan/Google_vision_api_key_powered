from Google_vision import image_analysis
image_path=str(input('Enter path name:'))
api_key=str(input('Enter api_key :'))

image=image_analysis(api_key,image_path)

Labels=image.labels
'''
The above statement will return a list of best descriptive words with
with the confidence values of each word prediction Eg:[('<description1>',0.91),('<description2>,0.82)...]
'''

web_labels=image.web_entities
'''
The above statement returns a list of words (with the respective confidence values) which describe the items in the internet that match with the image Eg:[('<description1>',0.91),('<description2>,0.82)...]
'''

text_detected=image.text_in_pic
"""
The above statement returns a string of textual content dedected in the image
Note: In case the api doesnt detect any image it returns a empty string
"""

title=image.best_description
'''
The above statement returns a string which contains a best description of the image
Note:The api will return a empty string incase where it cannot find one
'''
landmark_detected=image.landmark_properties
'''
The above statement returns a tuple with the landmark details
eg:('<landmark name>',0.92,{'latitude':<latitude value in float>,'longitude':<longitude value in float>'})
Note:It returns a empty tuple incase it doesnt detect any landmarks
'''
url_with_labels_search=image.labels_url()
'''
This returns a google search url based on the labels detected
'''
url_with_web_labels_search=image.web_entities_url()
'''
This returns a google search url based on the web labels detected
Note:In case of lack of web labels it raises a RuntimeError
'''
landmark_google_map_url=image.landmark_location_url()
'''
This returns a google map url with the landmark location
Note:Incase of lack of landmark details it raises a RuntimeError
'''

'''
In some cases labels are more accurate than web labels 
and in other cases web labels are more accurate than labels , 
hence one might give an option to users based on web labels or labels .

That's the reason behind proving urls for search results based on labels and web labels

web pages can be launched with webbrowser  module or with other alternatives
'''

'''
Note: The Google_vision.py file must be present in the same directory as  
the file where you use the module
 That's it Happy Coding!!!
'''

'''
Print the respective variable to see the results
'''