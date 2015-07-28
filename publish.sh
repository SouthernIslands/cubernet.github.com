#!/bin/bash
echo -n "Enter comment:"
read  comment
files=`git status | grep deleted | awk '{print \$2}'`
if [ "${files}" == "" ]; then
   echo "nothing to remove"
else
	for var in $files
	do
		git rm $var
	done
fi
git add .
git commit -m "$comment"
git push
exit 0