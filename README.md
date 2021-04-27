# Hexafuel-Oil
<h2>To run and test in local development:</h2>
<ul>
  <li>In terminal, change your current directory to which manage.py reside</li>
  <li>In terminal, type: <b>python manage.py runserver</b></li>
  <li>In your browser, go to: <b>http://127.0.0.1:8000/home</b></li>
</ul>

<h2>To run coverage test:</h2>
<ul>
  <li>Install Coverage.py from <a href="https://coverage.readthedocs.io/en/coverage-5.5/">here</a></li>
  <li>Coverage.py Explanation:  <a href="https://docs.google.com/document/d/1f2E76Hc1ax4pjL02YPOqhHs_jUr-5gyhqzBJKp3CyyM/edit?pli=1">Click Here</a></li>
  <li>change your terminal directory to <b>root/hexafuel_oil</b> where <b>manage.py</b> resides in</li>
  <li>run this command: <b>coverage run --source='.' manage.py test hexafuel_oil_app</b></li>
  <li>to get the coverage report, run: <b>coverage html</b> for the HTML version of the report, or <b>coverage report</b> for a quick overview of the coverage report in the terminal</li>
</ul>
