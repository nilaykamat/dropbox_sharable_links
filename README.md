# dropbox_sharable_links
Ths code snippet iterates through the folders provided in the code and generates sharable links for all files present in them.
<h3>How this works</h3>
<p>This utility will allow a user to generate the <strong>Sharable Links</strong> in Bulk for all the files within a given folder.</p>
<hr>
<h5>1. Generating API Key</h5>
<ul>
	<li>Log in to Dropbox</li>
	<li>Visit Link <a href="https://www.dropbox.com/developers/apps" target="_blank">https://www.dropbox.com/developers/apps</a></li>
	<li>Click on Create app (button to top right)</li>
	<li>Select the option <strong>"Dropbox API"</strong> (first option)</li>
	<li>Select the option <strong>"Full Dropbox"</strong></li>
	<li>Give an appropriate name to your app</li>
	<li>Once the app is created, Open it</li>
	<li>You have to click on the button to <strong>"Generate Access Token"</strong> which is present in the "OAuth2" section of the app</li>
	<li>Copy the token that is generated and save it somewhere</li>
	<li>This Token is used as the <strong>API Key</strong> in our application</li>
</ul>
<h5>2. Getting Folder Paths</h5>
<ul>
	<li>The folder paths should start with <strong>"/"</strong></li>
	<li>The folder path should be the path relative from the <strong>Dropbox Root Directory</strong></li>
	<li>If more than 1 folder paths are to be selected, then insert new folder path on a new line</li>
	<li>
		Example : <br>
		<code>/SS'18/Amazon/amazon 172 lot 5<br>/SS'18/Amazon/amazon 172 lot 6<br>/SS'18/Raymond Next/raymondnext 172</code>
	</li>
	<li>Each folder path will have a corresponding csv file generated</li>
	<li>All the files in the folder as well as all the sub-folders will generate sharable links</li>
	<li>Folder Paths are case sensitive. Please make sure you add proper casing and spaces while adding folder paths.</li>
</ul>