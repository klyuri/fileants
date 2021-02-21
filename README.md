# fileants
Work with your own files

## Stage 0. Concept development.

The work will be done in the **ideas** branch.

## Проблемная область

Проект не предназначен для файлов, которые представляют для себя высокую степень связанности. Например репозиторий исходного кода.

Большинство файлов самодостаточны. А с увеличением устройств растет количество носителей. При этом многие делят пространство на компютере на отдельные хранилища (разделы, жесткие диски).

Можно, конечно, использовать облачные технологии, но тогда надо иметь или всё в облаке, или держать полную копию облака на носителе. Размеры облаков не достаточны даже для хранения собственных фотографий.

Рассмотрим пример. Есть планшет. В нем есть SD-карта. Обычно это устройство для получения информации (чтения). Тогда на карту копируется выборка из хранилищ на компьютере. Но иногда на планшете загружаются новые файлы (из интернета или другого источника, например, фотоаппарата). Получается дилемма: или держать эти файлы отдельно от скопированных с компьютера или при синхронизации разбираться в дубликатах.

Для поиска дубликатов есть достаточно хороших программ, но я не встретил ни одной, чтобы она по предоставленному файлу ответила на вопрос: существует ли в месте хранения его копия.

Поэтому задумался над созданием данной программы.

## Текущий подход к решению

Программа UNIX-like. В смысле организации домашнего каталога.

В ~/.config/fileants хранится конфигурация.
В ~/.local/share/fileants хранится база.

### Терминология

Попытаюсь ввести терминологию в проекте.
Файл - это (ant) муравей.
Группа файлов - это (swarm) стая/рой. Муравьи путешествуют как по одиночке, так и стаями/роем.
Каждый муравей может жить в одном или нескольких муравейниках (hill).
Муравейники могут располагаться в лесу (forest).

Таким образом, имя муравья (ant) или их стаи (swarm) необходимо определить для каждого муравья (ant) его места в муравейниках (hill). Для поиска можно задать более крупное понятие лес (hill) или перечислить несколько лесов.

### Состав данных

#### Конфигурация

В конфигурации содержится:
  - общие настройки
  - перечень хранилищ hill и forest
  - для hill фильтры (исключений) (пока будут отсутсвовать)

#### База

В базе утилитой сохраняется информация об идексах файлов.

Одна индексная запись состоит из полей фиксированной длины:
  - размер файла
  - дата файла (пока не будет, не понятен запрос, может даже приводить к путанице)
  - первый индекс - md5 сумма начала файла (1K, 32K, 1M ? думаю будет определяться в конфигурации, пока нравится 1M)
  - второй индекс - sha1/sha256/... более сложная сумма по всему файлу
и поле произвольной длины:
  - имя файла (допустимы все символы, кроме перевода строки, при формировании такие файлы игнорируются и выводится предупреждение)

Индексы нарезаются на файлы.
?Как. Есть несколько идей. В первом варианте будет единый огромный файл.

### Работа

#### Конфигурация

В начале работы требуется задать hill.
Каждый hill может содержать несколько путей в файловой системе.
Замем можно при необходимости объединить в hill в firest. Суть forest - облегчение ввода типовых задач поиска.

fileants --hill
fileants --hill mycollection --create /path1/to/dir1 /path2/to/dir2
fileants --hill mycollection
fileants --hill mycollection --delete
fileants --forest
fileants --forest myphoto
fileants --forest myphoto --set mycollection1 mycollection2
fileants --forest myphoto --add mycollection3
fileants --forest myphoto --del mycollection2

#### Модификация базы

Базу можно формирорвать по частям.

Можно определить уровни:
- l0 - поиск только по размеру
- l1 - поиск по размеру и первому идексу
- l2 - поиск по размеру и двум первым индексам
- l9 - поиск полного соотвествия по содержимому

Можно формировать базу с различной нагрузкой на диск. То есть, в некоторых случаях может быть достаточно только размера файла, особенно при использовании при поиска l9 не мелких файлах. А в других случаях, например для фотоархива, достаточно сравнивать только l1. Уровень l9 хорошо подходит для работы с такими файлами, как ISO образ - если его посчитать, то при сравннии не потребуется производить тяжелое чтение. l2 можно формировать при l9 запросах изменяя по ходу работы базу.

Думаю такой подход с дополненеим индексов возможен и для заполнения остальных индексов. Хотя есть сомнения. Обычно, l2 требуется для больших фафлов, а для средних ~30-60M это будет малоэффективная трата процессорного времени.

fileants --hill mycollection1 --update 1
fileants --hill myiso --update 0
fileants --hill mycollection2 --check 0

#### Поиск

fileants --hill mycollection1 --file 0 /path/to/my_file
fileants --forest myphoto --dir 1 /path/to/my_album
fileants --forest myiso --dir 9 /path/to/my_iso_file
