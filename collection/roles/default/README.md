# Description
Provides host information gathering and connectivity validation.

# Using this role with tags
- `overview` Information about the inventory host
- `validate` Validate inventory host is reachable

# Example with role and tags
```yaml
- hosts: ...
  tasks:

    - name: Information about the inventory host
      import_role:
        name: enasisnetwork.utility.default
      tags: [overview]

    - name: Validate inventory host is reachable
      import_role:
        name: enasisnetwork.utility.default
      tags: [validate]
```

# Example from command line
*Information about the inventory host*
```
ansible-playbook \
  ...
  --tags "overview" \
  enasisnetwork.utility.default
```
*Validate inventory host is reachable*
```
ansible-playbook \
  ...
  --tags "validate" \
  enasisnetwork.utility.default
```
