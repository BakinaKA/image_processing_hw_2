# image_processing_hw_2
```
Выполнили: Бакина Ксения, Круглов Алексей.
Результаты обработки изображений расположены в таком порядке:
1 - исходное изображение 
2 - изображение после применения фильтра erode
3 - обработка изображения 2 с применением функции watershed
4 - изображение после применения фильтра fastNlMeansDenoisingColored
5 - обработка изображения 4 с применением функции watershed
6 - изображение после применения фильтра medianBlur
7 - обработка изображения 6 с применением функции watershed

Обработка изображений состоит из двух этапов:
1) Удаление шума с помощью трех разных фильтров(erode, fastNlMeansDenoisingColored, medianBlur)
  erode - размывает(операция сужения) изображение с использованием ядра(kernel)
  (изображение формируется из локальных минимумов — т.е. будут увеличиваться тёмные области)
  medianBlur - медианный фильтр - реализован с помощью скользящей подматрицы(ядра) определенной 
  размерности NxN пикселя. На вход он принимает N^2 значений (пикселей), а на выход выдаёт 
  одно, которое выбирается по следующему правилу: в отсортированном в порядке возрастания 
  последовательности входных пикселей выбирается серединный результат(медиану).
  fastNlMeansDenoisingColored - фильтр Non-Local Means(нелокальный сглаживающий фильтр) 
  находит похожие области изображения и применяет информацию из них для взаимного усреднения.
2) Сегментация изображений с помощью алгоритма водораздела(функции watershed)
  Для алгоритма водораздела нужно определить маркеры.
Маркеры - это пиксели, в которых мы уверены, что они принадлежат объектам,
присутствующим на изображении(с них начинается заливка).
В нашей задаче 3 маркера: здоровая часть листа, больная часть листа и фон.
В нашем решении мы отмечает здоровый лист и фон, а всё остальное считается поражениями листа.

Для каждого изображения подобраны свои маркеры. Это обусловлено многими 
факторами: листы на изображениях не всегда расположены посередине, каждый 
лист уникален, поэтому трудно подобрать именно те координаты, где находится 
здоровый участок листа, и самое важное на каждой фотографии разное освещение. 
Освещение играет огромную роль. На одних изображениях цвет листа ровный, без 
засветов, теней тоже не много, а на других множество засветов, теней, перепадов 
цвета, логично, что фильтры будут работать хуже. Например, на 3 и 5 изображениях 
освещение "плохое" для фильтров, они определяют черешок листа как больной 
участок. И добавление/изменение маркеров не исправило этого, иногда даже ухудшало результат.

Если посмотреть на код, то можно заметить, что размер kernel для каждого 
изображения разный. Это обусловлено тем, что фильтр erode очень чувствителен 
к изменению этого параметра. Для 1,3 и 7 изображения размер kernel равен 3, цвет 
листа достаточно хорошо отличим от больных участков. На зображенях 2,5,8 много 
засветов, цвет листа варьируется от темно-зеленого до почти белого, поэтому фильтры 
работают лучше на большем размере kernel. А также мы заметили, что размер ядра оптимальный 
для фильтра erode улучшает результат фильтра fastNlMeansDenoisingColored, если передавать
размер ядра в 3(h - параметр, регулирующий силу фильтра для яркостной составляющей) и 
4(templateWindowSize - размер в пикселях шаблона, который используется для вычисления
весов) параметрах.

У фильтров medianBlur и fastNlMeansDenoisingColored очень близки результаты, erode 
достаточно сильно отличается и чаще работает хуже остальных: определяет тень как поражение 
листа, а не часть фона. На одноих изображениях лист и фон хорошо отличимы, а на некоторых 
изображениях край листа настолько затемнён или засветлён, что при попытке устранения
неправильного определения тени часть листа тоже распознается как фон.
Фильтр medianBlur размывает изображение сильнее остальных фильтров. Где-то это помогает лучше точнее 
определить поражения листа, а где-то наоборот мешает распознаванию больных участков листа.
Например обратим внимание на изображение 5. По середине листа есть достаточно темные группы пикселей,
которые относятся к поражениям листа, хотя ими не являются. И лучше всех эти неточности убирает именно medianBlur.
Теперь посмотрим на изображение 1. В правой части листа есть совсем небольшие больные участки, erode и 
fastNlMeansDenoisingColored их определяют, а medianBlur нет.
По изображениям можно заметитить, что фильтр fastNlMeansDenoisingColored выдает средний результат между
результатами работы erode и medianBlur.
```

img 1:

![1](https://user-images.githubusercontent.com/61293111/138915851-92a71a97-3e5b-42a0-8ecf-a0edd50e88a1.jpg)

![1_moderode](https://user-images.githubusercontent.com/61293111/138961270-37958b97-0635-450d-b0f1-8fe2c66f624b.jpg)

![1_mod1](https://user-images.githubusercontent.com/61293111/138959154-a5f51788-3087-4186-9f2f-f0713eeb2d46.jpg)

![1_moddst](https://user-images.githubusercontent.com/61293111/138961315-d69c0d0e-1c90-4cb8-8d6b-6d825db97ff6.jpg)

![1_mod2](https://user-images.githubusercontent.com/61293111/138959183-2329917f-3f78-40df-8a68-dfbefed16250.jpg)

![1_modmedian](https://user-images.githubusercontent.com/61293111/138961348-a0d31115-fe0c-4d78-8949-17220526514f.jpg)

![1_mod3](https://user-images.githubusercontent.com/61293111/138959203-26498318-1c66-404c-b321-ddaa4e3707e2.jpg)

img 2:

![2](https://user-images.githubusercontent.com/61293111/138916051-d6cdc463-bdfe-46dd-a897-4782410e7497.jpg)

![2_moderode](https://user-images.githubusercontent.com/61293111/138961616-910e55ae-fd13-46be-bb79-6be264a3b14d.jpg)

![2_mod1](https://user-images.githubusercontent.com/61293111/138959235-a0858611-42ed-4777-9eaa-8fa897c08b1c.jpg)

![2_moddst](https://user-images.githubusercontent.com/61293111/138961633-a41e3e3f-d58f-4c3a-9944-14f34a632c4f.jpg)

![2_mod2](https://user-images.githubusercontent.com/61293111/138959257-07347a24-e4ca-4aa0-a3c0-3d0c0c27f0d1.jpg)

![2_modmedian](https://user-images.githubusercontent.com/61293111/138961648-19800b50-f081-46aa-8717-6fdac6440582.jpg)

![2_mod3](https://user-images.githubusercontent.com/61293111/138959278-f8271996-3904-4f97-8daf-aeed588f84cc.jpg)

img 3:

![3](https://user-images.githubusercontent.com/61293111/138916190-e22bb902-bbf3-4fb1-8129-35f87b8c4ed5.jpg)

![3_moderode](https://user-images.githubusercontent.com/61293111/138961664-e8f1f350-5ea1-4a0e-b4ef-a7e5028c04c7.jpg)

![3_mod1](https://user-images.githubusercontent.com/61293111/138959312-78017eab-97c1-48ea-8bfa-c11dc01b0a46.jpg)

![3_moddst](https://user-images.githubusercontent.com/61293111/138961679-b9fab282-cf40-408d-83fe-598861c0a27b.jpg)

![3_mod2](https://user-images.githubusercontent.com/61293111/138959328-4389a4f8-6e78-4b10-9c73-e49c4f9e5089.jpg)

![3_modmedian](https://user-images.githubusercontent.com/61293111/138961698-3605505f-e998-49f4-8271-04d4c2853179.jpg)

![3_mod3](https://user-images.githubusercontent.com/61293111/138959348-347c1f83-02bc-4f28-b89a-cb3e70586c00.jpg)

img 5:

![5](https://user-images.githubusercontent.com/61293111/138916270-a9fdaea1-c00c-492e-9c8e-3bcbe324d027.JPG)

![5_moderode](https://user-images.githubusercontent.com/61293111/138961744-84e29b59-9bb3-4806-9a83-d3a8316e6cdf.jpg)

![5_mod1](https://user-images.githubusercontent.com/61293111/138959384-72c242ae-5442-4da9-889e-677d118ab121.jpg)

![5_moddst](https://user-images.githubusercontent.com/61293111/138961756-fd72628b-f0f7-4676-b035-e07e4c66d278.jpg)

![5_mod2](https://user-images.githubusercontent.com/61293111/138959403-8962a36b-38cb-4573-8533-9a78e5020c7e.jpg)

![5_modmedian](https://user-images.githubusercontent.com/61293111/138961765-6e9fc8aa-3b46-4660-b97f-a4c01ad2afe6.jpg)

![5_mod3](https://user-images.githubusercontent.com/61293111/138959421-4795d855-d678-47b4-a85b-4addcb7c5cb3.jpg)

img 7:

![7](https://user-images.githubusercontent.com/61293111/138916351-bc2720de-b36e-450a-9851-5a67b5e71999.JPG)

![7_moddst](https://user-images.githubusercontent.com/61293111/138961784-eeef9d37-a7bd-4f0b-9958-2998b5e98998.jpg)

![7_mod1](https://user-images.githubusercontent.com/61293111/138959439-e7654c5e-0c02-43cc-8d4f-7f3a392851b1.jpg)

![7_moderode](https://user-images.githubusercontent.com/61293111/138961795-d6ff9dd8-f3c8-4337-87de-83ed978589f3.jpg)

![7_mod2](https://user-images.githubusercontent.com/61293111/138959463-7bbdbc5c-f4dd-4c71-9ee7-62aba907fde9.jpg)

![7_modmedian](https://user-images.githubusercontent.com/61293111/138961812-d2c8b89a-bf5d-4c5c-b398-d3a1f4a180bc.jpg)

![7_mod3](https://user-images.githubusercontent.com/61293111/138959490-805570ad-7da4-400a-9147-96b3afe86345.jpg)

img 8:

![8](https://user-images.githubusercontent.com/61293111/138916421-4cfa5c3a-2d88-44ee-b093-39a0041e9c42.JPG)

![8_moddst](https://user-images.githubusercontent.com/61293111/138961846-e57aa464-86e1-4bbd-93f0-d499c4653c7f.jpg)

![8_mod1](https://user-images.githubusercontent.com/61293111/138959522-14a78d44-5e73-4f14-a65d-077c7cf4f144.jpg)

![8_moderode](https://user-images.githubusercontent.com/61293111/138961864-d1e28c38-08de-45b5-a8d3-14139ddd012d.jpg)

![8_mod2](https://user-images.githubusercontent.com/61293111/138959536-7fd89a25-ca80-4c66-88fc-69f041f8cadd.jpg)

![8_modmedian](https://user-images.githubusercontent.com/61293111/138961879-e7a6b89d-37c8-4150-988d-ee3cb1bda1c2.jpg)

![8_mod3](https://user-images.githubusercontent.com/61293111/138959566-7109b42c-fdc2-44d5-970c-c7edb634c963.jpg)
