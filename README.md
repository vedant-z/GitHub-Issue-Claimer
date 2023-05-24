# GitHub-Issue-Claimer


Video Demo: https://drive.google.com/drive/folders/1sDYCmxRspyxv0toeP7URL87WFy1Jv1Zw?usp=sharing
(Please do increase the quality if not visible clearly.)

Above script runs forever looking out for new issues(multiple allowed) with required label. Initially before starting the script we claim one of the issue
with the required label by commenting on it and we add the exact TITLE and LINK of that issue in "issues.txt" file so as to facilitate the conditions
for it to run ideally.

After that we start the script. Now the script will traverse over issues, let's say no new issues have arrived then the script will traverse through
old issues until it reaches the issue we had claimed initially. It will check if the label of that issue is matching with required label and
obviously it is the issue with required label as we have already claimed it, now according to code it will enter the if condition and retrieve the
issue link to check if that link is already present in the "issues.txt" file and yes it will be present as we have manually added it. Now as it is
present then we will break out of the for loop as our goal is to claim any issue only once. So the driver will sleep for 10 minutes and again retrieve
the ISSUE page to check for new issues.

Now let's say 3 new issues were uploaded while driver and we were were sleeping. As usual the script will run, also we know that we haven't claimed
any new issue with desired label except the one we claimed manually, so the "issues.txt" file still has only one issue title and link. So script
will traverse through issues one by one this time new ones as well(also keep one thing in mind the new issues will appear on top so we will be traversing
from top only which is the desired condition to get latest issues). Now while traversing if any issue has required label then we will check if it has
already been claimed by checking if that issue link is present in "issues.txt" file, but we know as we will be traversing the new issues first no link
will be present in file so we claim it and add the issue link and title in file. This will continue till we reach the old issue(1st one which we manually added)
and as soon as we reach that issue we break and driver sleeps again for 10 minutes.

Now if one of the 3 new issues which had arrived had the required label then we would have claimed it and now the top claimed issue is the point upto which script will
traverse in future and this will ensure that any issue is claimed only once.


Example:

Here the "X" infront of any issue means it doesn't have required label.

Initial configuration:

Issue 3 X
Issue 2 (One with required label and which we claimed manually)
Issue 1 X

First time script runs with no new issue:

Issue 3 X
Issue 2 (Already claimed)
Issue 1 X

Script will traverse till issue 2 and break to restart at that issue as it is already claimed and we assume all the required issues below it(Old ones) are already
claimed.

Second time script runs with 3 new issues:

Issue 6 X
Issue 5
Issue 4
Issue 3 X
Issue 2 (Claimed) (Breaking point)
Issue 1 X

We traverse from issue 6 and claim issue 5,4 with their links added and we break at issue 2. Now the Breaking point will be issue no.5

Issue 6 X
Issue 5 (Claimed) (Breaking point)
Issue 4 (Claimed)
Issue 3 X
Issue 2 (Claimed)
Issue 1 X
