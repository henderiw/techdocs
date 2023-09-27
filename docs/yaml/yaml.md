# yaml

open api is described in yaml or json

YAML ain't Markup Language

- less verbose, but uses indentiation like python
- spaces are used for identation
- types are determined from context
- strings don't need to be quoted unless we have to make it explicit "11.47"
- lists -> you dont need to declare the list
- multi-line strings: 
    - | means preserve lines and spaces
    - > means fols lines
    - |-
    - |+
- `#` for comments
- $ref to indicate a reference

```yaml
schema:
  $ref: '#/definitions/user'
...
definitions:
  user:
    required:
    - username
    - id
  properties:
    username:
      type: string
    id:
      type: integer
    format: int64
```