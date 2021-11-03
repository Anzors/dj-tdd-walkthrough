from django.http import response
from django.test import TestCase
from django.test import TestCase 
from selenium import webdriver
from .forms import HashForm
import hashlib
from .models import Hash
from django.core.exceptions import ValidationError


# Create your tests here.

# class FunctionalTestCase(TestCase):

#     #Define things to do at start of test
#     def setUp(self):
#         self.browser=webdriver.Firefox()

#     #Must start with test_
#     def test_there_is_homepage(self):
#         # Fetch a page - note use of django default port - so this is the home page

#         self.browser.get("http://localhost:8000")
#         # look for the text box on the home page
#         self.assertIn('Enter hash here', self.browser.page_source)

#     def test_hash_hello(self):
#         #Fetch the page
#         self.browser.get("http://localhost:8000")
#         # get the text box to enter some data in
#         text =self.browser.find_element_by_id('id_text')
#         #enter the text 'hello' into that text box
#         text.send_keys('hello')
#         #send a click event
#         self.browser.find_element_by_name('submit').click()
#         #check that the SHA256 of that string is output
#         self.assertIn('2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824', self.browser.page_source)

#     #Define stuff to do when we finish
#     def tearDown(self):
#         # close the browser
#         self.browser.quit()

class UnitTestsfunctional(TestCase):

    def test_hash_form(self):
        form = HashForm(data={'text':'hello'})
        self.assertTrue(form.is_valid())

    def test_hash_function_works(self):
        text_hash = hashlib.sha256('hello' .encode('utf-8')).hexdigest()
        self.assertEqual('2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824', text_hash)

    def storeHashOfHello(self):
        #Create a hash of 'hello'
        hashobj = Hash()
        hashobj.text = 'hello'
        hashobj.hash = '2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824'

        #Store in the database
        hashobj.save()
        return hashobj

    def test_hash_object(self):
        hashobj = self.storeHashOfHello()

        #Retrieve and cheeck the text is correct
        hashpulled = Hash.objects.get(hash='2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824')
        self.assertEqual(hashpulled.text, hashobj.text)

    def test_view_of_hash(self):
        self.storeHashOfHello()

        response = self.client.get('/hash/2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824')
        self.assertContains(response, 'hello')

    def test_bad_hash(self):
        def bad_hash():
            hashobj = Hash()
            hashobj.hash = '2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824gggToLong'
            hashobj.full_clean()
        self.assertRaises(ValidationError, bad_hash)



