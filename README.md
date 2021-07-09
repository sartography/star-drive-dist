
# This is terrible crap.  It should be a docker container, or at least a set of shell scripts.  We can't install docker on the servers at UVA currently.  So we deploy to production by pushing to this star-drive-dist directory, and then pulling from these repos on production. Potentially running some flask commands if required.

# Release-It
We are using Release-It to manage pushing code that can be easily
deployed to staging and production.  You can read more about the project
here: https://www.npmjs.com/package/release-it

I'll bet you skimmed that quick!  I'll bet you didn't read it carefully!  It took me at least 5 re-reads, so let me tell you the important bit, and save you some time.  At a minimum, you will need to follow these directions to set up your local environment to handle github releases:
https://www.npmjs.com/package/release-it#github-releases

Once Release-it is installed and you have a github token setup per those instructions, use it to create
a tag.




# But I am actually am a pain.
for instance, I expect that beside this directory, you have checked out the star-drive repository, and called it star-drive.

# Say you took some steps like:

* cd ../star-drive
* cd frontend
* ng build --prod -c production

That would create a whole pile of cool, pre-complied, ready to deploy angular wonder, that is darn near ready for production.  But Wait!  There is more!

If you did that, then you can run these commands that will set up this star-drive dist:
``` bash
rm -rf backend
rm -rf frontend
cp -r ../star-drive/frontend/dist/star-drive/ frontend/
cp -r ../star-drive/backend backend
rm -rf backend/python-env
rm -rf backend/__pycache__/
git add backend
git add frontend
```










