# AWS CLI in Docker for openshift
Containerized AWS CLI on alpine for use with cronjobs in openshift container platform 3.7

##Usage

Clone this reposiry, edit scripts/backup.sh and insert your aws commands. Use send_email.py as a bolerplate for sending email.
Edit cronjobs.yaml and add PVC that you want to backup to S3

Create the image
oc new-app <your-cloned-repo> --name="aws-cli"
oc delete dc aws-cli
oc delete svs aws-cli

Start the cron job
on create -f cronjobs.yml


## References

AWS CLI Docs: https://aws.amazon.com/documentation/cli/



