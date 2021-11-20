.PHONY: pull_from_prod deploy

pull_from_prod:
	scp yoga@jonc.yoga:/home/yoga/yoga-site/yoga-site.db .
	scp -r yoga@jonc.yoga:/home/yoga/yoga-site/media .
	scp -r yoga@jonc.yoga:/home/yoga/yoga-site/static .

deploy:
	cd deploy && ansible-playbook ansible_deploy.yml -i hosts --key-file yoga -K
