# pulumi
Using Pulumi and GitLab CI/CD to provision S3 infrastructure and automate the deployment of a static HTML file to AWS S3.

## Getting Start
1. Go to your gitlab => Setting ==> CI/CD ==> Variables and then create some necessary variable
`AWS_ACCESS_KEY_ID` your AWS access key id
`AWS_SECRET_ACCESS_KEY` your AWS secret access key
`PULUMI_ACCESS_TOKEN` your access token to connect to your pulumi account
2. Go to your gitlab and create your develop branch, or you can edit [.gitlab-ci.yml](.gitlab-ci.yml) file to change branch for deployment
3. Push code to your develop branch and merge
4. Go to your gitlab ==> Build ==> Pipelines to view deployment process


