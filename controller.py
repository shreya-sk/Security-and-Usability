'''
    This file will handle our typical Bottle requests and responses
    You should not have anything beyond basic page loads, handling forms and
    maybe some simple program logic
'''

from bottle import route, get, post, error, request, static_file

import model
import re


@route('/img/<picture:path>')
def serve_pictures(picture):
    '''
        serve_pictures

        Serves images from static/img/

        :: picture :: A path to the requested picture

        Returns a static file object containing the requested picture
    '''
    return static_file(picture, root='static/img/')

#-----------------------------------------------------------------------------

@post('/css_post')
def get_css_post():

    title = request.forms.get('title')
    description = request.forms.get('description')

    return model.forum_css_post(title, description)

@get('/users')
def users():
    return model.usersAll()

@post('/users')
def get_userdeleted():
    '''
        post_login

        Handles login attempts
        Expects a form containing 'username' and 'password' fields
    '''

    # Handle the form processing
    name = request.forms.get('name')
    print(name)

    return model.delete_user(name)

@post('/python_post')
def get_python_post():

    title = request.forms.get('title')
    description = request.forms.get('description')

    return model.forum_python_post(title, description)

@post('/tech_post')
def get_tech_post():

    title = request.forms.get('title')
    description = request.forms.get('description')

    return model.forum_tech_post(title, description)

@post('/java_post')
def get_java_post():

    title = request.forms.get('title')
    description = request.forms.get('description')

    return model.forum_java_post(title, description)


# Allow CSS
@route('/css/<css:path>')
def serve_css(css):
    '''
        serve_css

        Serves css from static/css/

        :: css :: A path to the requested css

        Returns a static file object containing the requested css
    '''
    return static_file(css, root='static/css/')

#-----------------------------------------------------------------------------
# Allow javascript
@route('/js/<js:path>')
def serve_js(js):
    '''
        serve_js

        Serves js from static/js/

        :: js :: A path to the requested javascript

        Returns a static file object containing the requested javascript
    '''
    return static_file(js, root='static/js/')

# Redirect to login
@get('/')
@get('/home')
def get_index():
    '''
        get_index

        Serves the index page
    '''
    return model.index()

@get('/seeposts')
def get_posts():
    '''
        get_index

        Serves the index page
    '''
    return model.seeposts()

@get('/forum')
def get_forum():
    return model.forum()

@get('/logout')
def get_logout():
    '''
        get_index

        Serves the index page
    '''
    return model.logout()
#-----------------------------------------------------------------------------

# Display the login page
@get('/login')
def get_login_controller():
    '''
        get_login

        Serves the login page
    '''
    return model.login_form()



# Display the login page
@get('/python')
def get_python_controller():
    '''
        get_signup

        Serves the signup page
    '''
    return model.forum_python()

@get('/java')
def get_java_controller():
    '''
        get_signup

        Serves the signup page
    '''
    return model.forum_java()

@get('/css')
def get_css_controller():
    '''
        get_signup

        Serves the signup page
    '''
    return model.forum_css()

@get('/signup')
def get_signup_controller():
    '''
        get_signup

        Serves the signup page
    '''
    return model.signup_form()

@get('/tech')
def get_tech_controller():
    '''
        get_signup

        Serves the signup page
    '''
    return model.form_tech()

#-----------------------------------------------------------------------------

# Attempt the login
@post('/login')
def post_login():
    '''
        post_login

        Handles login attempts
        Expects a form containing 'username' and 'password' fields
    '''

    # Handle the form processing
    username = request.forms.get('username')
    password = request.forms.get('password')

    # Call the appropriate method
    return model.login_check(username, password)


    # return model.messageEnc(postdata)



@post('/signup')

def post_signup():
    '''
        post_signup

        Handles login attempts
        Expects a form containing 'username' and 'password' fields
    '''

    # Handle the form processing
    # count = int( request.cookies.get('counter', '0') )
    # count += 1
    # response.set_cookie('counter', str(count))
    # print('You visited this page %d times' % count)

    username = request.forms.get('username')
    password = request.forms.get('password')



    # print(username, password)
    # Call the appropriate method
    return model.signup_check(username, password)



#-----------------------------------------------------------------------------


# @get('/inbox')
# def get_inbox():
#     return model.inbox_check()


# @post('/receiver')
# def get_receiver():
#     '''
#         post_login

#         Handles login attempts
#         Expects a form containing 'username' and 'password' fields
#     '''

#     # Handle the form processing
#     name = request.forms.get('name')
#     # message = request.forms.get('message')

#     # print(name, message)


#     return model.Receiver(name)

# @post('/message')
# def get_message():
#     '''
#         post_login
#
#         Handles login attempts
#         Expects a form containing 'username' and 'password' fields
#     '''
#
#     # Handle the form processing
#     # name = request.forms.get('name')
#     message = request.forms.get('message')
#
#     # print(name, message)
#
#
#     return model.Receiver(name)


# @get('/message')
# def message():
#     '''
#         post_login
#
#         Handles login attempts
#         Expects a form containing 'username' and 'password' fields
#     '''
#
#     # Handle the form processing
#
#     return model.Message()


@get('/about')
def get_about():
    '''
        get_about

        Serves the about page
    '''
    return model.about()

#-----------------------------------------------------------------------------

@get('/contactus')
def get_contact():
    '''
        get_contact

        Serves the contact us page
    '''
    return model.contact()
#-----------------------------------------------------------------------------


# Help with debugging
@post('/debug/<cmd:path>')
def post_debug(cmd):
    return model.debug(cmd)

#-----------------------------------------------------------------------------

# 404 errors, use the same trick for other types of errors
@error(404)
def error(error):
    return model.handle_errors(error)
