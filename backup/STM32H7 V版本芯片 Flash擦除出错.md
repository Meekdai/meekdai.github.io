STM32H7系列单片机主频已经高达480MHz，甚至有的已经标550MHz，通过LTDC和DMA2D控制800*480分辨率的屏幕以及很轻松了。老版本的H7芯片都是Y版本的，主频是400MHz，现在官方升级了V版本的，与Y的区别可以见官方[AN5312][1]文档。

这里我们主要碰到的是通过[dfu-util][2]，或者是ST官方的DfuSeDemo给芯片下载固件的时候，在擦除Flash的时候失败的问题。

dfu-util的Tickets里面已经记录了这个BUG，但是目前没有解决。官方的DfuSeDemo没有做修复，但是新的下载工具[STM32CubeProgrammer][3]，记录了更新修复[STM32CubeProgrammer release v2.6.0][4]

所以我们目前只能通过V2.6版本及以上的STM32CubeProgrammer程序给STM32H7的V版本芯片下载固件。

  [1]: https://www.st.com/content/ccc/resource/technical/document/application_note/group1/95/22/7c/0c/57/de/4b/f9/DM00609692/files/DM00609692.pdf/jcr:content/translations/en.DM00609692.pdf
  [2]: https://sourceforge.net/projects/dfu-util/
  [3]: https://www.st.com/content/st_com/en/products/development-tools/software-development-tools/stm32-software-development-tools/stm32-programmers/stm32cubeprog.html
  [4]: https://www.st.com/resource/en/release_note/dm00441049-stm32cubeprogrammer-release-v240-stmicroelectronics.pdf

[comment]: # (##{"timestamp":1612659540,"fontSize":"20px"}##)