#!/usr/bin/env bash

# Clear out what we have now
rm -rf backend/
rm -rf frontend/

# Assumes this is next to the star-drive checkout.
cd ../star-drive/frontend
ng build --prod -c production
cd ../../star-drive-dist/
cp -r ../star-drive/frontend/dist/star-drive/ frontend/
cp -r ../star-drive/backend backend
rm -rf backend/python-env
rm -rf backend/.idea
rm -rf backend/instance
rm -rf backend/tests
rm -rf star_drive.log
rm -rf __pycache__/
git add backend
git add frontend
