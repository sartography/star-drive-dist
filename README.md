You don't have to read all this crap.  It's going to lead you down a dark road my friend.  One that only those that have accepted the twilight truth of system administration need see.  Save yourself.  Just write code.  Don't look too deeply into this.  It seems easy to you now.  Simple.  Just leave it at that.  Don't delve.  Don't do it.  Stay naive as long as you can, and cherish those moments.  When they are gone, the are gone forever.  I write this with pain.  It took hours of late nights away from me that I could have otherwise spent advancing my early demise with alcohol and elicit drugs.  But I decided, no, no, the stress of system administration, that's how I want to accelerate my decrepitude.  That's the life for me! But not you.  You get to fall asleep to the soft chirps of crickets, and wake up each day to sunlight and the twitter of gentle birds as the soft breeze of summer tickles you into the consciousness of one more day of blissful ignorance to the horrible truth.  You are not standing on the back of one system administrator.  No.  You rest quietly in a hammock, strung betwixt trees that were fostered out of the soil of of 50 feet of expired system administrators.  Rocking gently in the breeze, smiling at the sun against your gentle skin.


# Release-It
We are using Release-It to manage pushing code that can be easily
deployed to staging and production.  You can read more about the project
here: https://www.npmjs.com/package/release-it

I'll bet you skimmed that quick!  I'll bet you didn't read it carefully!  It took me at least 5 re-reads, so let me tell you the important bit, and save you some time.  At a minimum, you will need to follow these directions to set up your local environment to handle github releases:
https://www.npmjs.com/package/release-it#github-releases


# That was kind.
This is just a section to remind you. I am a kind person.  You should like me.  Buy me some chocolate. Did you read that last part?  You did?  Did you follow it?  Don't ask me about it later.  I'll bite you.

# But I am actually am a pain.
for instance, I expect that beside this directory, you have checked out the star-drive repository, and called it star-drive.

# Say you took some steps like:

* cd ../star-drive
* cd frontend
* ng build --prod -c production

That would create a whole pile of cool, pre-complied, ready to deploy angular wonder, that is darn near ready for production.  But Wait!  There is more!



If you did that, then you can run this command:
cp -r ../star-drive/frontend/dist/star-drive/ frontend/
cp -r ../star-drive/backend backend
rm -rf backend/python-env
rm -rf __pycache__/










