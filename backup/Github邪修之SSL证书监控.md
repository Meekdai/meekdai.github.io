白嫖的3个月免费证书虽好，奈何时间太短，容易忘记更新，这不就有网友来提醒了 https://github.com/Meekdai/Gmeek/issues/274 。之前记得阿里云有邮件提醒的，最近突然没有提醒了，然后发现域名监控发邮件功能居然收费了24元，无奈只好自己再想想法子了。

作为一名不完全合格的Github邪修，当然是要在Github上开发这个功能了。因为ChatGPT日益强大，所以这种简单功能的代码部分完全交给它就行。

```
name: SSL Certificate Expiry

on:
  schedule:
    - cron: "0 16 * * *"
  workflow_dispatch: # 允许手动触发

jobs:
  check-ssl-cert:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout repo
        uses: actions/checkout@v4

      - name: Check SSL expiry
        id: ssl
        run: |
          DOMAIN="meekdai.com"
          EXPIRY_DATE=$(echo | openssl s_client -servername $DOMAIN -connect $DOMAIN:443 2>/dev/null \
            | openssl x509 -noout -enddate | cut -d= -f2)
          EXPIRY_TS=$(date -d "$EXPIRY_DATE" +%s)
          NOW_TS=$(date +%s)
          REMAINING_DAYS=$(( (EXPIRY_TS - NOW_TS) / 86400 ))

          if [ "$REMAINING_DAYS" -lt 7 ]; then
            STATUS="⚠️ meekdai.com 证书将在 $REMAINING_DAYS 天内过期！"
            echo "exit_needed=true" >> $GITHUB_OUTPUT
          else
            STATUS="✅ meekdai.com 证书正常，剩余 $REMAINING_DAYS 天"
            echo "exit_needed=false" >> $GITHUB_OUTPUT
          fi

          echo "status=$STATUS" >> $GITHUB_OUTPUT

      - name: Overwrite README.md with status
        run: |
          echo "${{ steps.ssl.outputs.status }}" > README.md

      - name: Commit and push if changed
        run: |
          git config user.name github-actions
          git config user.email github-actions@github.com

          if [[ `git status --porcelain` ]]; then
            git add README.md
            git commit -m "更新 SSL 证书状态"
            git push
          else
            echo "README 无变化，无需提交"
          fi

      - name: Fail if cert expires soon
        if: ${{ steps.ssl.outputs.exit_needed == 'true' }}
        run: |
          echo "❌ meekdai.com SSL 证书将在 ${{ steps.ssl.outputs.status }} 过期，触发失败"
          exit 1
```

巧妙的是这里利用了GitHub Action运行失败会自动给GitHub绑定的邮箱发送邮件的功能，所以不需要自己在添加邮件发送功能，或者是其他的webhook功能。

有道是越简单越强大，设置了每天运行一次Action，如果域名证书的时间大于7天，则不报错，更新readme文档中的时间即可；如果域名证书的时间小于7天了，更新readme文档中的时间，然后报错，触发GitHub发送邮件。

这样我就简单的实现了我所需要的全部功能，后续如果要添加多个域名证书检测也是很简单的，哈哈。然后根据习惯，我把这个项目命名为[GSSL](https://github.com/Meekdai/GSSL)