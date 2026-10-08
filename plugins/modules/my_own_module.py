#!/usr/bin/python

from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = r'''
---
module: my_own_module

short_description: Create or update a text file

version_added: "1.0.0"

description:
  - Creates a text file on the target host.
  - Updates the file when its content differs.
  - Does nothing when the file already contains the required content.

options:
  path:
    description:
      - Path to the text file on the target host.
    required: true
    type: str

  content:
    description:
      - Content that should be written to the file.
    required: true
    type: str

author:
  - kumarina-max
'''

EXAMPLES = r'''
- name: Create a text file
  my_own_namespace.yandex_cloud_elk.my_own_module:
    path: /tmp/my_test.txt
    content: "Hello from my own Ansible module!"
'''

RETURN = r'''
path:
  description:
    - Path to the managed file.
  type: str
  returned: always

content:
  description:
    - Content written to the file.
  type: str
  returned: always
'''

from ansible.module_utils.basic import AnsibleModule


def run_module():

    module_args = dict(
        path=dict(type='str', required=True),
        content=dict(type='str', required=True)
    )

    result = dict(
        changed=False,
        path='',
        content=''
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    path = module.params['path']
    content = module.params['content']

    result['path'] = path
    result['content'] = content

    if module.check_mode:
        module.exit_json(**result)

    try:
        with open(path, 'r', encoding='utf-8') as file:
            current_content = file.read()

        if current_content != content:
            with open(path, 'w', encoding='utf-8') as file:
                file.write(content)

            result['changed'] = True

    except FileNotFoundError:
        with open(path, 'w', encoding='utf-8') as file:
            file.write(content)

        result['changed'] = True

    except OSError as error:
        module.fail_json(
            msg=f'Unable to manage file {path}: {error}',
            **result
        )

    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()
