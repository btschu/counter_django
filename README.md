# counter_django

## Objectives:

- Practice using session to store data about a particular client's history with the app
- Be able to check whether a session exists
- Be able to initialize a session
- Be able to modify a session

Build a Django application that counts the number of times the root route ('/') has been viewed. 

This assignment is to test your understanding of session.

<img width="321" alt="Screen Shot 2022-04-20 at 11 48 46 AM" src="https://user-images.githubusercontent.com/92617960/164291782-8bde91f6-18ab-4d60-a0eb-2a567d55c0a6.png">

As part of this assignment, please start with the following features first:

- localhost:8000 - have the template render the number of times the client has visited this site
- localhost:8000/destroy_session - Clear the session. Once cleared, redirect to the root.

Some Helpful Tips
We can't increment something that doesn't exist! Here's how to check if a key exists in session yet:

```py
if 'key_name' in request.session:
    print('key exists!')
else:
    print("key 'key_name' does NOT exist")
```

If we want to get rid of what is currently stored in session:

```py
del request.session['key_name']	# clears a specific key
```

- [ ] Create a new Django project called counter

- [ ] Have the root route render a template that displays the number of times the client has visited this site. Refresh the page several times to ensure the counter is working.

- [ ] Add a "/destroy_session" route that clears the session and redirects to the root route. Test it.

- [ ] NINJA BONUS: Add a Reset button that uses the "/destroy_session" route

- [ ] NINJA BONUS: Add a +2 button underneath the counter and a new route that will increment the counter by 2

- [ ] SENSEI BONUS: Add a form that allows the user to specify the increment of the counter and have the counter increment accordingly

- [ ] SENSEI BONUS: Adjust your code to display both how many times the user has actually visited the page, as well as the value of the counter, given the above functionality
