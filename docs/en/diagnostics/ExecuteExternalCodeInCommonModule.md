# Executing of external code in a common module on the server (ExecuteExternalCodeInCommonModule)

| Type | Scope | Severity | Activated<br/>by default | Minutes<br/>to fix | Tags |
| :-: | :-: | :-: | :-: | :-: | :-: |
| `Security Hotspot` | `BSL` | `Critical` | `Yes` | `15` | `badpractice`<br/>`standard` |

<!-- Блоки выше заполняются автоматически, не трогать -->
## Description
<!-- Описание диагностики заполняется вручную. Необходимо понятным языком описать смысл и схему работу -->

## Examples
<!-- В данном разделе приводятся примеры, на которые диагностика срабатывает, а также можно привести пример, как можно исправить ситуацию -->

## Sources
<!-- Необходимо указывать ссылки на все источники, из которых почерпнута информация для создания диагностики -->


## Snippets

<!-- Блоки ниже заполняются автоматически, не трогать -->
### Diagnostic ignorance in code

```bsl
// BSLLS:ExecuteExternalCodeInCommonModule-off
// BSLLS:ExecuteExternalCodeInCommonModule-on
```

### Parameter for config

```json
"ExecuteExternalCodeInCommonModule": false
```