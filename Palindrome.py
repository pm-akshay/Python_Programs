#wap to check if the string is palindrome or not
st=input('Enter string:')
s=st.lower()
rev=s[::-1]
if s==rev:
    print('This is a palindrome')
else:
    print('Not a palindrome')
