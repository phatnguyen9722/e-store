### What is CSRF
- That is `Cross Site Request Forgery` </br>
- VN calls "Giả mạo Request" </br>

#### Overview
- CSRF is an attack that forces an end user to execute unwanted actions on a web application in which they’re currently authenticated. </br>
- With a little help of social engineering (such as sending a link via email or chat), an attacker may trick the users of a web application into executing actions of the attacker’s choosing. </br>
- If the victim is a normal user, a successful CSRF attack can force the user to perform state changing requests like transferring funds, changing their email address, and so forth. If the victim is an administrative account, CSRF can compromise the entire web application. </br>
- Example: Attacker give you a link in fb, you click and login in the opened login form 👉 Poor your Account 🥲

#### How it works in Django
----
- Add {% csrf_token %} as a child of form template (html file contains form)
- Look at Login page 
