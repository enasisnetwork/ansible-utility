# Functions and routines associated with Enasis Network Orchestrations.

# This file is part of Enasis Network software eco-system. Distribution
# is permitted, for more information consult the project license file.



.PHONY: utility-overview
utility-overview: \
	.check-stage .check-limit
	@## Information about the inventory host
	@#
	$(call MAKE_PR2NT,\
		<cD>make <cL>utility-overview<c0>)
	@#
	@( \
		set -e; \
		[ -f ./orchestro.env ] \
			&& set -a \
			&& . ./orchestro.env \
			&& set +a || true; \
		. $(VENVP)/bin/activate; \
		PYTHONPATH=. \
		ansible-playbook \
			$(ansible_args) \
			--limit="localhost,$(limit)" \
			--tags=overview \
			enasisnetwork.utility.default; \
		deactivate)



.PHONY: utility-validate
utility-validate: \
	.check-stage .check-limit
	@## Validate inventory host is reachable
	@#
	$(call MAKE_PR2NT,\
		<cD>make <cL>utility-validate<c0>)
	@#
	@( \
		set -e; \
		[ -f ./orchestro.env ] \
			&& set -a \
			&& . ./orchestro.env \
			&& set +a || true; \
		. $(VENVP)/bin/activate; \
		PYTHONPATH=. \
		ansible-playbook \
			$(ansible_args) \
			--limit="localhost,$(limit)" \
			--tags=validate \
			enasisnetwork.utility.default; \
		deactivate)
