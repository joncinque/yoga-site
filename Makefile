.PHONY: pull_from_prod deploy

pull_from_prod:
	scp yoga@joncyoga.com:/home/yoga/yoga-site/yoga-site.db .
	scp -r yoga@joncyoga.com:/home/yoga/yoga-site/media .
	scp -r yoga@joncyoga.com:/home/yoga/yoga-site/static .

deploy:
	cd deploy && ansible_playbook ansible_deploy.yml -i hosts --key-file yoga -K
