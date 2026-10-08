# my_own_role

Роль для создания и обновления текстового файла с использованием модуля `my_own_module` из коллекции `my_own_namespace.yandex_cloud_elk`.

## Требования

- Ansible Core 2.19+
- Python 3.12+
- Коллекция `my_own_namespace.yandex_cloud_elk`

## Переменные роли

| Переменная | Значение по умолчанию | Описание |
|---|---|---|
| `path` | `/tmp/my_own_module_playbook.txt` | Путь к создаваемому файлу |
| `content` | `Hello from Ansible custom module!` | Содержимое файла |

Переменные определены в `defaults/main.yml` и могут быть переопределены при использовании роли.

## Зависимости

Дополнительные роли не требуются.

## Используемый модуль

Роль использует модуль:

`my_own_namespace.yandex_cloud_elk.my_own_module`

Модуль создаёт файл, если он отсутствует, и обновляет его содержимое, если оно отличается от заданного.

При повторном запуске с теми же параметрами изменения не выполняются.

## Пример использования

    ---
    - name: Use my own role
      hosts: localhost
      connection: local
      gather_facts: false

      roles:
        - my_own_namespace.yandex_cloud_elk.my_own_role

## Переопределение переменных

Переменные роли можно изменить непосредственно в playbook:

    ---
    - name: Create custom file
      hosts: localhost
      connection: local
      gather_facts: false

      vars:
        path: /tmp/custom.txt
        content: "Custom content"

      roles:
        - my_own_namespace.yandex_cloud_elk.my_own_role

## Структура роли

    my_own_role/
    ├── defaults/
    │   └── main.yml
    ├── handlers/
    │   └── main.yml
    ├── meta/
    │   └── main.yml
    ├── README.md
    ├── tasks/
    │   └── main.yml
    ├── tests/
    │   ├── inventory
    │   └── test.yml
    └── vars/
        └── main.yml

## Идемпотентность

Роль является идемпотентной благодаря используемому модулю.

При первом запуске файл создаётся или изменяется:

    changed: [localhost]

При повторном запуске с теми же параметрами изменений нет:

    ok: [localhost]

## Лицензия

MIT

## Автор

kumarina-max
