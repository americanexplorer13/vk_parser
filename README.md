# vk_likes
You will need: Python ver 3.6 and high, but I recommend to use python 3.7
external libraries: vk-api, pandas
import vk-api
import pandas

After installing, open the code and go to the 16 string: 

vk_session = vk_api.VkApi('__email_vk__', '__password__', auth_handler=auth_handler)

and execute the program,

Appear first message, input the code from 2factor auth (If you have it)
Appear second message, input friend id which we will parse. 

The result of the work will be save in CSV format file. 

# What we can collect

We can easily collect comments, likes, audio, video and music from people until their profiles are not hidden from the public
The most basic task is to collect likes, 'cause vk API has specific method to check if our user liked something or not.
The medium task is to collect comments from specific user 'cause as far as I understood, we should do it by ourself and vk doesn't provide any methods to do this task easier. 

# What we cannot collect

I guess there is no such thing that we cannot collect, but there can be a problem if the specific user is hidden from public, so it's physically impossible to take any information from him. Or another problem if specific user has public account but his friends doesn't or they are all hidden by user's security politics. 
