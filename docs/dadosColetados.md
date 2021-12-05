# Dados Coletados API

## Insersão de dados
Adiciona os dados coletados para o usuário informado.

*URL*: `/api/add`

*Method*: `POST`

*Permissão*: `Nenhuma`

## Parâmetros

```json
{
    "id_user": "ID Usuário",
    "valor1": "Float",
    "valor2": "Float",
    "tipo": "TC / PA / SP02"
}
```

## Retorno Sucesso
*Condição*: Todos os dados estão corretos.

*Código*: `201 CREATED`

```json
{
    "id_user": 1,
    "valor1": 37.5,
    "valor2": 0,
    "tipo": "TC"
}
```

## Retorno Falha
*Condição*: Caso algum valor esteja faltando || Usuário informado não está cadastrado.

*Código*: `400 BAD REQUEST`

```json
{
    "ERROR":"Error Message", 
    "Status":400
}
```
