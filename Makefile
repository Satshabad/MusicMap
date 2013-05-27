test:
	nosetests ${SINGLETEST} --nocapture -i '^(it|ensure|must|should|specs?|examples?|deve)' -i '(specs?(.py)?|examles?(.py)?)' '--with-spec' '--spec-color'
