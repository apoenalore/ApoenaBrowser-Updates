# Apoena Browser — Atualizações Android

Este repositório **público** serve somente para distribuir atualizações oficiais do aplicativo Android Apoena Browser. O código-fonte principal continua no repositório privado `apoenalore/ApoenaBrowser`.

## Estado inicial

O arquivo `updates/latest.json` está publicado, porém **não existe APK oficial assinado publicado**. Portanto, o aplicativo não deve apresentar uma atualização disponível ainda.

## Publicar uma versão

1. No Godot, exporte em **modo Release (sem depuração)** com o pacote fixo `com.apoena.browser`, a mesma chave de assinatura permanente, `versionCode` crescente e `minSdk 29` até revisão do plugin.
2. Faça um backup seguro da chave `.jks` fora do repositório e nunca inclua senhas ou `export_presets.cfg` com dados sensíveis no Git.
3. Crie uma **GitHub Release** neste repositório, com tag como `v0.3.1-alpha` e **um único APK assinado** anexado como ativo (asset) da Release.
4. A automação `Publicar manifesto de atualização` tenta calcular o SHA-256 e atualizar `updates/latest.json` quando a Release é publicada. Se o GitHub Actions não executar, use o script `tools/gerar_manifest_release.py` e envie o JSON atualizado manualmente.
5. Antes de divulgar, teste a instalação em um aparelho Android. A primeira Release assinada pode exigir a remoção de uma instalação antiga assinada com a chave **Debug**.

### Endereço público consultado pelo aplicativo

`https://raw.githubusercontent.com/apoenalore/ApoenaBrowser-Updates/main/updates/latest.json`

Requisitos de atualização: versão maior no manifesto, URL de APK originada de Releases deste repositório, SHA-256 correto, mesmo pacote Android e assinatura compatível. O usuário autoriza o download e a instalação; não há instalação silenciosa.

**Importante:** um repositório público expõe os APKs e o manifesto. **Não publique chaves, senhas, dados pessoais, tokens, arquivos confidenciais ou código-fonte privado.**
