dll = [
    # 简体中文
    """更新日志（v0.10.0及之后）
v0.14.2
统一解析 API 返回码，兼容旧响应格式，修复多个功能的 status_code 异常，并处理超时、HTTP 错误和无效响应。
修复音频、主播、电磁力和直播签到的接口路径。评论改用分页接口，关闭粉丝监控窗口后会停止请求。
v0.14.1
直接显示登录二维码，并在手机确认后自动登录。可选择本地保存登录状态，下次启动自动读取。
按用户名片接口的返回格式修复“查询用户信息”，并处理查询失败和缺失字段。
v0.14.0
在 v0.13.1 基础上继续更新
新增高 DPI 支持：程序会读取系统 DPI 缩放比例，界面、字号与控件间距自动缩放，高分屏下不再模糊
启动时自动读取系统语言并切换界面，不再弹窗要求输入语言代号
initialize.txt 现在只用于设定初始字体，其中的语言代号不再生效
补齐其余 12 种语言的更新日志（此前缺少 v0.12.0 至 v0.13.1）
修复西班牙语、印尼语下更新日志强制显示英文的问题
全面校对并补齐 13 种语言的界面文本，修正误翻与英语占位，并修复因文本条目缺失导致的崩溃
v0.13.1
终版，停止更新
v0.13.0
更多功能支持繁体中文opencc自动翻译
修复了最新版Python环境下，无法打开简繁转换器的bug，但是此功能现在仍然无法正常转换（输出文本和输入文本完全相同）
修复了更改自定义字体时若点击取消后界面变为默认宋体的bug
添加了退出确认界面、更改字体时输入非法数字的提示界面
v0.12.0
修正部分文本内容
格式化代码，使其更具有可读性
开始测试抛出B站api中的错误
将大部分组件移入“requirements”文件夹下（因为initialize.txt是可选组件，所以没有移动）
注意：
1.由于文本修整，“登录用户信息”中的大多数多语言文本被去除并且用英语代替，后续会补回来。
2.预计下个版本将直接过渡到1.0.0的面向对象程序，不兼容旧版。
v0.11.1
合并部分功能代码，缩小程序体积
增加了查询用户关注和用户粉丝的功能（需要登录，因此放到了“登录用户操作”功能下）
修复了日语模式下“其他工具（Other tools）”窗口打开时没有按钮并且报错的问题
查询UP主视频状态中增加了电磁力数据
注意：v1.0.0将会全面将程序面向对象化，更加开源
v0.11.0
使用opencc模块实现繁体中文下的文本简繁转换，使繁体中文模式覆盖更加全面（OpenCC项目地址：https://github.com/BYVoid/OpenCC）
取消pyglet模块的需求。
修复了退出程序时，用户粉丝实时变动数据框无法关闭并保持无响应的问题
修正了部分繁体中文文本
一定程度上继续完善了各个功能的多语言支持
当网络不稳定导致请求失败时将会多次重试，直到成功或者失败100次。
v0.10.1
锁定了窗口尺寸，防止手动更改导致排版出现问题
重新洗牌更新日志
优化按钮文本和关于界面的文字处理方式
尝试直接运行组件时会增加提示
对于未开发语言的文本，将用英语占位
注意：从v0.11.0开始，将会完全弃用pyglet模块，并在未来采用新的更改界面字体的方式，降低程序冗杂度
v0.10.0
更改了字体设定逻辑
版本号规范化为x.y.z形式
""",
    # 英语
    """Update log (v0.10.0 and later)
v0.14.2
Normalize API response codes, fix status_code errors, and handle timeouts, HTTP errors and invalid responses.
Repair the audio, streamer, creator rating and live check-in endpoints. Use paginated comments and stop polling when the fan monitor closes.
v0.14.1
Display the login QR code in the app and sign in after phone confirmation. Optionally remember the login across restarts.
Fix user lookup to read the user card response and handle errors and missing fields.
v0.14.0
Continuing development on top of v0.13.1
Added high-DPI support: the program reads the system DPI scale and scales the interface, fonts and widget spacing accordingly, so it is no longer blurry on high-DPI screens
The interface language is now detected from the system language at startup, with no more dialog asking for a language number
initialize.txt now only sets the initial font; the language number in it is no longer used
Completed the update logs of the other 12 languages (v0.12.0 to v0.13.1 were missing)
Fixed the update log being forced to English in Spanish and Indonesian
Audited and completed the UI text in all 13 languages, corrected mistranslations and English placeholders, and fixed crashes caused by missing text entries
v0.13.1
Final version; development has stopped
v0.13.0
More features now support automatic OpenCC conversion to Traditional Chinese
Fixed a bug that prevented the Simplified/Traditional Chinese converter from opening under the latest Python version, but the converter still cannot convert correctly (the output text is identical to the input text)
Fixed a bug where the interface fell back to the default SimSun font after clicking Cancel while changing the custom font
Added an exit confirmation dialog and a warning dialog for invalid numbers entered when changing the font
v0.12.0
Corrected some text
Reformatted the code to make it more readable
Began testing the surfacing of errors returned by the Bilibili API
Moved most components into the "requirements" folder (initialize.txt was not moved because it is optional)
Note:
1. Because of the text cleanup, most of the multilingual text in "Logged user info" was removed and replaced with English; it will be restored later.
2. The next version is expected to move directly to a 1.0.0 object-oriented program, which will not be compatible with older versions.
v0.11.1
Merged some function code to reduce the program size
Added the ability to query a user's following list and fan list (login required, so it is placed under "Logged user operation")
Fixed the error where the "Other tools" window opened in Japanese mode with no buttons
Added electromagnetic force data to the UP master's video status query
Note: v1.0.0 will turn the program fully object-oriented and make it more open-source
v0.11.0
Using the OpenCC module to convert text into Traditional Chinese, making Traditional Chinese mode coverage more comprehensive (OpenCC project address: https://github.com/BYVoid/OpenCC)
Dropped the requirement for the pyglet module.
Fixed the issue where the real-time fan count window could not be closed and became unresponsive when exiting the program
Revised some Traditional Chinese text
Further improved multilingual support for each function
When a request fails because the network is unstable, it is now retried until it succeeds or 100 attempts have failed
v0.10.1
Locked the window size to prevent layout problems caused by manual resizing
Redesigned the update log
Optimized the text of buttons and the "About" interface
A hint is now shown when a component is run directly
For text in languages that have not been developed yet, English is used as a placeholder
Note: Starting from v0.11.0, the pyglet module will be completely abandoned and a new way of changing the interface font will be adopted to reduce program complexity
v0.10.0
Changed the font setting logic
Normalized version numbers to the x.y.z format
""",
    # 繁体中文
    """更新日誌（v0.10.0及之後）
v0.14.2
統一解析 API 回傳碼，相容舊格式，修復 status_code 例外，並處理逾時、HTTP 錯誤和無效回應。
修正音訊、直播主、電磁力及直播簽到的 API 路徑。留言改用分頁 API，關閉粉絲監控視窗後會停止請求。
v0.14.1
直接顯示登入 QR Code，在手機確認後自動登入。可選擇在本機儲存登入狀態，下次啟動時自動讀取。
依照使用者名片 API 的回應格式修復「查詢使用者資訊」，並處理錯誤和缺少的欄位。
v0.14.0
在 v0.13.1 基礎上繼續更新
新增高 DPI 支援：程式會讀取系統 DPI 縮放比例，介面、字型與元件間距自動縮放，高解析度螢幕下不再模糊
啟動時自動讀取系統語言並切換介面，不再彈窗要求輸入語言代號
initialize.txt 現在只用於設定初始字型，其中的語言代號不再生效
補齊其餘 12 種語言的更新日誌（先前缺少 v0.12.0 至 v0.13.1）
修復西班牙語、印尼語下更新日誌強制顯示英文的問題
全面校對並補齊 13 種語言的介面文字，修正誤譯與英語佔位，並修復因文字條目缺失導致的崩潰
v0.13.1
終版，停止更新
v0.13.0
更多功能支援繁體中文opencc自動翻譯
修復了最新版Python環境下，無法開啟簡繁轉換器的bug，但是此功能現在仍然無法正常轉換（輸出文字和輸入文字完全相同）
修復了更改自訂字型時若點擊取消後介面變為預設宋體的bug
新增了退出確認介面、更改字型時輸入非法數字的提示介面
v0.12.0
修正部分文字內容
格式化程式碼，使其更具可讀性
開始測試拋出B站api中的錯誤
將大部分元件移入「requirements」資料夾下（因為initialize.txt是選用元件，所以沒有移動）
注意：
1.由於文字修整，「登入使用者資訊」中的大多數多語言文字被去除並且用英語代替，後續會補回來。
2.預計下個版本將直接過渡到1.0.0的物件導向程式，不相容舊版。
v0.11.1
合併部分功能程式碼，縮小程式體積
增加了查詢使用者關注和使用者粉絲的功能（需要登入，因此放到了「登入使用者操作」功能下）
修復了日語模式下「其他工具（Other tools）」視窗開啟時沒有按鈕並且報錯的問題
查詢UP主影片狀態中增加了電磁力資料
注意：v1.0.0將會全面將程式物件導向化，更加開源
v0.11.0
使用opencc模組實現繁體中文下的文字簡繁轉換，使繁體中文模式覆蓋更加全面（OpenCC專案地址：https://github.com/BYVoid/OpenCC）
取消pyglet模組的需求。
修復了退出程式時，使用者粉絲即時變動資料框無法關閉並保持無回應的問題
修正了部分繁體中文文字
一定程度上繼續完善了各個功能的多語言支援
當網路不穩定導致請求失敗時將會多次重試，直到成功或者失敗100次。
v0.10.1
鎖定了視窗尺寸，防止手動更改導致排版出現問題
重新洗牌更新日誌
優化按鈕文字和「關於」介面的文字處理方式
嘗試直接執行元件時會顯示提示
對於未開發語言的文字，將用英語佔位
注意：從v0.11.0開始，將會完全棄用pyglet模組，並在未來採用新的更改介面字型的方式，降低程式冗雜度
v0.10.0
更改了字型設定邏輯
版本號規範化為x.y.z形式
""",
    # 日语
    """更新ログ（v0.10.0以降）
v0.14.2
APIの応答コードの処理を統一し、旧形式と異常応答に対応しました。
音声・配信者などのAPIを修正し、コメントのページ表示とファン数監視の終了処理を改善しました。
v0.14.1
ログイン用QRコードを表示し、スマートフォンでの確認後にログインします。ログイン状態は端末に保存できます。
ユーザー情報の取得を修正し、エラーや欠落項目を処理します。
v0.14.0
v0.13.1 をベースに更新を継続
高 DPI 対応を追加：システムの DPI 倍率を読み取り、画面・フォント・部品の間隔を自動的に拡大縮小するため、高解像度ディスプレイでもぼやけません
起動時にシステム言語を自動的に読み取って画面言語を切り替え、言語番号の入力を求めるダイアログを表示しなくなりました
initialize.txt は初期フォントの設定のみに使用され、言語番号は無効になりました
残り 12 言語の更新ログを補完（これまで v0.12.0～v0.13.1 が欠落）
スペイン語・インドネシア語で更新ログが強制的に英語表示される問題を修正
13言語すべての画面テキストを校正・補完し、誤訳と英語のプレースホルダーを修正するとともに、テキスト項目の欠落によるクラッシュを修正
v0.13.1
最終版、更新を終了
v0.13.0
より多くの機能が繁体字中国語へのOpenCC自動変換に対応
最新のPython環境で簡繁変換ツールを開けないバグを修正。ただし、この機能は現在も正常に変換できません（出力テキストが入力テキストと完全に同じです）
カスタムフォントの変更時にキャンセルを押すと画面が既定の宋体（SimSun）に戻るバグを修正
終了確認画面、フォント変更時に無効な数字を入力した場合の警告画面を追加
v0.12.0
一部のテキストを修正
コードを整形し、可読性を向上
Bilibili API のエラーを送出するテストを開始
ほとんどのコンポーネントを「requirements」フォルダへ移動（initialize.txt は任意コンポーネントのため移動していません）
注：
1.テキスト整理のため、「ログインユーザー情報」内の多言語テキストの大部分が削除され、英語に置き換えられました。後日補完します。
2.次のバージョンでは1.0.0のオブジェクト指向プログラムへ直接移行する予定で、旧バージョンとの互換性はありません。
v0.11.1
いくつかの機能コードをマージしてプログラムサイズを縮小
ユーザーがフォローしているユーザーとそのファンの一覧を照会する機能を追加（ログインが必要なため、「ログインユーザー操作」機能の下に配置）
「その他のツール」ウィンドウを日本語モードで開いたときにボタンが表示されずエラーになる問題を修正
UP主の動画ステータス照会に電磁力データを追加
注：v1.0.0 ではプログラムを全面的にオブジェクト指向化し、よりオープンソース化します
v0.11.0
OpenCCモジュールを使用して繁体字中国語へのテキスト変換を実現し、繁体字中国語モードのカバー範囲をより包括的にしました（OpenCCプロジェクトアドレス：https://github.com/BYVoid/OpenCC）
pygletモジュールの要件を廃止。
プログラム終了時に、ユーザーのファン数のリアルタイムデータボックスを閉じられず応答しなくなる問題を修正
繁体字中国語のテキストを一部修正
各機能の多言語対応をある程度継続的に改善
ネットワークが不安定でリクエストが失敗した場合、成功するか100回失敗するまで再試行するようにしました
v0.10.1
手動でのサイズ変更によるレイアウトの乱れを防ぐため、ウィンドウサイズを固定
更新ログを再構成
ボタンのテキストと「バージョン情報」画面のテキスト処理を最適化
コンポーネントを直接実行しようとすると警告が表示されるように
未開発の言語のテキストには英語をプレースホルダーとして使用
注：v0.11.0 以降、pyglet モジュールは完全に廃止され、プログラムの複雑さを軽減するためにインターフェースフォントを変更する新しい方法が採用されます
v0.10.0
フォント設定ロジックを変更
バージョン番号を x.y.z 形式に正規化
""",
    # 德语
    """Änderungsprotokoll (v0.10.0 und höher)
v0.14.2
API-Rückgabecodes werden einheitlich verarbeitet. Zeitüberschreitungen und ungültige Antworten werden abgefangen.
Mehrere Endpunkte wurden korrigiert. Kommentare werden seitenweise geladen und die Fanüberwachung endet beim Schließen.
v0.14.1
Der Anmelde-QR-Code wird direkt angezeigt. Die Anmeldung kann lokal gespeichert werden.
Die Benutzerabfrage verarbeitet die Profilantwort sowie Fehler und fehlende Felder korrekt.
v0.14.0
Weiterentwicklung auf Basis von v0.13.1
High-DPI-Unterstützung hinzugefügt: Das Programm liest den DPI-Faktor des Systems und skaliert Oberfläche, Schriftarten und Abstände entsprechend, sodass es auf hochauflösenden Bildschirmen nicht mehr unscharf ist
Die Oberflächensprache wird beim Start automatisch aus der Systemsprache ermittelt; die Abfrage einer Sprachnummer entfällt
initialize.txt dient jetzt nur noch zur Einstellung der Anfangsschriftart; die Sprachnummer darin wird nicht mehr verwendet
Die Änderungsprotokolle der übrigen 12 Sprachen vervollständigt (v0.12.0 bis v0.13.1 fehlten bisher)
Fehler behoben, durch den das Änderungsprotokoll in Spanisch und Indonesisch zwangsweise auf Englisch angezeigt wurde
Die Oberflächentexte aller 13 Sprachen wurden geprüft und vervollständigt, Fehlübersetzungen und englische Platzhalter korrigiert sowie Abstürze durch fehlende Texteinträge behoben
v0.13.1
Letzte Version, Entwicklung eingestellt
v0.13.0
Weitere Funktionen unterstützen die automatische OpenCC-Konvertierung ins traditionelle Chinesisch
Fehler behoben, durch den sich der Konverter für vereinfachtes/traditionelles Chinesisch unter der neuesten Python-Version nicht öffnen ließ; die Konvertierung funktioniert derzeit aber weiterhin nicht korrekt (Ausgabetext und Eingabetext sind identisch)
Fehler behoben, durch den die Oberfläche nach einem Klick auf „Abbrechen“ beim Ändern der benutzerdefinierten Schriftart auf die Standardschrift SimSun zurückfiel
Dialog zur Bestätigung des Beendens sowie Hinweisdialog bei ungültigen Zahleneingaben beim Ändern der Schriftart hinzugefügt
v0.12.0
Einige Texte korrigiert
Code formatiert, um die Lesbarkeit zu verbessern
Mit dem Testen der Fehlerausgabe der Bilibili-API begonnen
Die meisten Komponenten in den Ordner „requirements“ verschoben (initialize.txt wurde nicht verschoben, da es optional ist)
Hinweis:
1. Aufgrund der Textüberarbeitung wurde der Großteil der mehrsprachigen Texte in „Angemeldete Benutzerinformationen“ entfernt und durch Englisch ersetzt; dies wird später wieder ergänzt.
2. Die nächste Version wird voraussichtlich direkt auf ein objektorientiertes Programm der Version 1.0.0 umsteigen, das nicht mit älteren Versionen kompatibel ist.
v0.11.1
Einige Funktionscodes zusammengeführt, um die Programmgröße zu verringern
Funktion zur Abfrage der gefolgten Nutzer und der Fans eines Benutzers hinzugefügt (Anmeldung erforderlich, daher unter der Funktion „Angemeldete Benutzeroperationen“)
Fehler behoben, bei dem das Fenster „Andere Tools“ im japanischen Modus ohne Schaltflächen und mit einer Fehlermeldung geöffnet wurde
Daten zur elektromagnetischen Kraft in der Statusabfrage der UP-Videos ergänzt
Hinweis: v1.0.0 wird das Programm vollständig objektorientiert und quelloffener machen
v0.11.0
Verwendung des OpenCC-Moduls zur Textkonvertierung ins traditionelle Chinesisch, wodurch die Abdeckung des traditionellen chinesischen Modus umfassender wird (OpenCC-Projektadresse: https://github.com/BYVoid/OpenCC)
Die Anforderung des pyglet-Moduls entfällt.
Fehler behoben, bei dem sich das Echtzeit-Datenfenster der Fan-Zahlen beim Beenden des Programms nicht schließen ließ und nicht reagierte
Einige traditionelle chinesische Texte überarbeitet
Die mehrsprachige Unterstützung der einzelnen Funktionen weiter verbessert
Bei instabiler Netzwerkverbindung werden fehlgeschlagene Anfragen bis zu 100-mal wiederholt
v0.10.1
Fenstergröße gesperrt, um Layoutprobleme durch manuelles Ändern zu vermeiden
Das Änderungsprotokoll neu gestaltet
Textverarbeitung für Schaltflächen und die „Über“-Oberfläche optimiert
Beim direkten Ausführen einer Komponente wird nun ein Hinweis angezeigt
Für Texte in nicht entwickelten Sprachen wird Englisch als Platzhalter verwendet
Hinweis: Ab v0.11.0 wird das pyglet-Modul vollständig aufgegeben und eine neue Möglichkeit zum Ändern der Oberflächenschriftart eingeführt, um die Programmkomplexität zu verringern
v0.10.0
Logik für die Schriftarteneinstellung geändert
Versionsnummern auf das Format x.y.z normalisiert
""",
    # 法语
    """Journal des mises à jour (v0.10.0 et versions ultérieures)
v0.14.2
Les codes de réponse de l’API sont traités de manière uniforme, y compris les erreurs et les délais dépassés.
Plusieurs points d’accès ont été corrigés. Les commentaires sont paginés et le suivi des abonnés s’arrête à la fermeture.
v0.14.1
Le code QR de connexion s’affiche dans l’application. La session peut être enregistrée sur l’appareil.
La consultation des profils gère correctement la réponse, les erreurs et les champs manquants.
v0.14.0
Poursuite du développement sur la base de la v0.13.1
Ajout de la prise en charge des écrans à haute densité (High DPI) : le programme lit le facteur d’échelle du système et adapte l’interface, les polices et les espacements, qui ne sont plus flous sur les écrans haute résolution
La langue de l’interface est désormais détectée automatiquement à partir de la langue du système au démarrage ; la boîte de dialogue demandant un numéro de langue a été supprimée
initialize.txt ne sert plus qu’à définir la police initiale ; le numéro de langue qu’il contient n’est plus utilisé
Les journaux de mise à jour des 12 autres langues ont été complétés (v0.12.0 à v0.13.1 manquaient)
Correction du journal des mises à jour affiché de force en anglais en espagnol et en indonésien
Révision et complétion des textes d’interface dans les 13 langues, correction des erreurs de traduction et des textes provisoires en anglais, et correction des plantages dus à des entrées manquantes
v0.13.1
Version finale, développement arrêté
v0.13.0
Davantage de fonctions prennent en charge la conversion automatique en chinois traditionnel via OpenCC
Correction d’un bug empêchant l’ouverture du convertisseur simplifié/traditionnel avec la dernière version de Python ; la conversion ne fonctionne toutefois toujours pas correctement (le texte de sortie est identique au texte saisi)
Correction d’un bug où l’interface revenait à la police SimSun par défaut après un clic sur « Annuler » lors du changement de police personnalisée
Ajout d’une fenêtre de confirmation de fermeture et d’un avertissement en cas de saisie d’un nombre invalide lors du changement de police
v0.12.0
Correction de certains textes
Reformatage du code pour le rendre plus lisible
Début des tests de remontée des erreurs de l’API Bilibili
Déplacement de la plupart des composants dans le dossier « requirements » (initialize.txt n’a pas été déplacé car il est facultatif)
Remarque :
1. En raison du nettoyage des textes, la plupart des textes multilingues de « Informations de l’utilisateur connecté » ont été supprimés et remplacés par de l’anglais ; ils seront rétablis ultérieurement.
2. La prochaine version devrait passer directement à un programme orienté objet en 1.0.0, incompatible avec les anciennes versions.
v0.11.1
Fusion de certains codes fonctionnels pour réduire la taille du programme
Ajout de la fonction d’interrogation des abonnements et des abonnés d’un utilisateur (nécessitant une connexion, donc placée sous la fonction « Opérations de l’utilisateur connecté »)
Correction du problème d’absence de boutons et de message d’erreur à l’ouverture de la fenêtre « Autres outils » en mode japonais
Ajout de données de force électromagnétique à l’état des vidéos de l’UP
Remarque : la v1.0.0 rendra entièrement le programme orienté objet et plus open-source
v0.11.0
Utilisation du module OpenCC pour convertir le texte en chinois traditionnel, ce qui rend la couverture du mode chinois traditionnel plus complète (adresse du projet OpenCC : https://github.com/BYVoid/OpenCC)
Suppression de la dépendance au module pyglet.
Correction du problème où la fenêtre de données en temps réel du nombre d’abonnés ne pouvait pas être fermée et ne répondait plus à la fermeture du programme
Révision de certains textes en chinois traditionnel
Amélioration continue de la prise en charge multilingue de chaque fonction
En cas d’échec d’une requête dû à un réseau instable, elle est désormais réessayée jusqu’à sa réussite ou 100 échecs
v0.10.1
Taille de la fenêtre verrouillée pour éviter les problèmes de mise en page dus à un redimensionnement manuel
Journal des mises à jour remanié
Optimisation du texte des boutons et de l’interface « À propos »
Un avertissement s’affiche désormais lorsqu’un composant est exécuté directement
Pour les textes dans les langues non développées, l’anglais est utilisé comme espace réservé
Remarque : à partir de la v0.11.0, le module pyglet sera complètement abandonné et une nouvelle façon de changer la police de l’interface sera adoptée pour réduire la complexité du programme
v0.10.0
Modification de la logique de réglage des polices
Normalisation des numéros de version au format x.y.z
""",
    # 泰语
    """บันทึกการอัปเดต (v0.10.0 เป็นต้นไป)
v0.14.2
ปรับการอ่านรหัสตอบกลับ API ให้เป็นแบบเดียวกันและรองรับข้อผิดพลาด
แก้ไขปลายทาง API หลายรายการ เปลี่ยนเป็นการโหลดความคิดเห็นแบบแบ่งหน้า และหยุดตรวจสอบผู้ติดตามเมื่อปิดหน้าต่าง
v0.14.1
แสดงคิวอาร์โค้ดสำหรับเข้าสู่ระบบในแอปและเลือกบันทึกการเข้าสู่ระบบในเครื่องได้
แก้ไขการค้นหาข้อมูลผู้ใช้และการจัดการข้อผิดพลาดหรือข้อมูลที่ขาดหาย
v0.14.0
อัปเดตต่อจาก v0.13.1
เพิ่มการรองรับหน้าจอความละเอียดสูง (High DPI): โปรแกรมจะอ่านอัตราการขยายของระบบและปรับอินเทอร์เฟซ ฟอนต์ และระยะห่างขององค์ประกอบให้ขยายตามอัตโนมัติ จึงไม่เบลอบนหน้าจอความละเอียดสูงอีกต่อไป
ระบบจะอ่านภาษาของระบบโดยอัตโนมัติเมื่อเริ่มต้นและสลับภาษาอินเทอร์เฟซให้ ไม่มีหน้าต่างให้กรอกหมายเลขภาษาอีกแล้ว
initialize.txt ใช้กำหนดฟอนต์เริ่มต้นเท่านั้น หมายเลขภาษาในไฟล์นี้ไม่มีผลแล้ว
เพิ่มบันทึกการอัปเดตของอีก 12 ภาษาที่ขาดไป (v0.12.0 ถึง v0.13.1)
แก้ไขปัญหาที่บันทึกการอัปเดตแสดงเป็นภาษาอังกฤษเสมอในภาษาสเปนและอินโดนีเซีย
ตรวจทานและเติมข้อความอินเทอร์เฟซให้ครบทั้ง 13 ภาษา แก้ไขการแปลผิดและข้อความภาษาอังกฤษที่ใช้แทน และแก้ไขการแครชที่เกิดจากรายการข้อความขาดหาย
v0.13.1
เวอร์ชันสุดท้าย หยุดพัฒนาแล้ว
v0.13.0
ฟังก์ชันเพิ่มเติมรองรับการแปลงเป็นภาษาจีนตัวเต็มอัตโนมัติด้วย OpenCC
แก้ไขบั๊กที่ไม่สามารถเปิดตัวแปลงจีนตัวย่อ/ตัวเต็มได้ในสภาพแวดล้อม Python เวอร์ชันล่าสุด แต่ฟังก์ชันนี้ยังคงแปลงไม่ถูกต้อง (ข้อความที่แสดงออกมาเหมือนกับข้อความที่ป้อนทั้งหมด)
แก้ไขบั๊กที่หน้าจอกลับไปใช้ฟอนต์ SimSun ค่าเริ่มต้นหลังจากกดยกเลิกเมื่อเปลี่ยนฟอนต์ที่กำหนดเอง
เพิ่มหน้าต่างยืนยันการออกและหน้าต่างแจ้งเตือนเมื่อกรอกตัวเลขไม่ถูกต้องขณะเปลี่ยนฟอนต์
v0.12.0
แก้ไขเนื้อหาข้อความบางส่วน
จัดรูปแบบโค้ดใหม่ให้อ่านง่ายขึ้น
เริ่มทดสอบการโยนข้อผิดพลาดจาก API ของ Bilibili
ย้ายคอมโพเนนต์ส่วนใหญ่ไปไว้ในโฟลเดอร์ "requirements" (ไม่ได้ย้าย initialize.txt เนื่องจากเป็นคอมโพเนนต์เสริม)
หมายเหตุ:
1. เนื่องจากการปรับปรุงข้อความ ข้อความหลายภาษาใน "ข้อมูลผู้ใช้ที่เข้าสู่ระบบ" ส่วนใหญ่ถูกลบและแทนที่ด้วยภาษาอังกฤษ ซึ่งจะเติมกลับในภายหลัง
2. เวอร์ชันถัดไปคาดว่าจะเปลี่ยนไปใช้โปรแกรมเชิงวัตถุเวอร์ชัน 1.0.0 โดยตรง และไม่รองรับเวอร์ชันเก่า
v0.11.1
รวมโค้ดฟังก์ชันบางส่วนเข้าด้วยกันเพื่อลดขนาดโปรแกรม
เพิ่มฟังก์ชันสอบถามรายชื่อผู้ใช้ที่ติดตามและรายชื่อแฟนคลับของผู้ใช้ (ต้องเข้าสู่ระบบ จึงอยู่ในฟังก์ชัน "การดำเนินการของผู้ใช้ที่เข้าสู่ระบบ")
แก้ไขปัญหาที่หน้าต่าง "เครื่องมืออื่นๆ" ไม่มีปุ่มและเกิดข้อผิดพลาดเมื่อเปิดในโหมดภาษาญี่ปุ่น
เพิ่มข้อมูลแรงแม่เหล็กไฟฟ้าในการสอบถามสถานะวิดีโอของ UP
หมายเหตุ: v1.0.0 จะเปลี่ยนโปรแกรมเป็นเชิงวัตถุทั้งหมดและเปิดโอเพนซอร์สมากขึ้น
v0.11.0
ใช้โมดูล OpenCC ในการแปลงข้อความเป็นภาษาจีนตัวเต็ม ทำให้โหมดภาษาจีนตัวเต็มครอบคลุมมากขึ้น (ที่อยู่โครงการ OpenCC: https://github.com/BYVoid/OpenCC)
ยกเลิกความจำเป็นในการใช้โมดูล pyglet
แก้ไขปัญหาที่กล่องข้อมูลแบบเรียลไทม์ของจำนวนแฟนคลับไม่สามารถปิดได้และค้างไม่ตอบสนองเมื่อออกจากโปรแกรม
แก้ไขข้อความภาษาจีนตัวเต็มบางส่วน
ปรับปรุงการรองรับหลายภาษาของฟังก์ชันต่างๆ อย่างต่อเนื่อง
เมื่อเครือข่ายไม่เสถียรและคำขอล้มเหลว โปรแกรมจะลองใหม่หลายครั้งจนกว่าจะสำเร็จหรือล้มเหลวครบ 100 ครั้ง
v0.10.1
ล็อกขนาดหน้าต่างเพื่อป้องกันปัญหาเลย์เอาต์จากการปรับขนาดด้วยตนเอง
จัดเรียงบันทึกการอัปเดตใหม่
ปรับปรุงการจัดการข้อความของปุ่มและหน้าต่าง "เกี่ยวกับ"
แสดงข้อความแจ้งเตือนเมื่อพยายามเรียกใช้คอมโพเนนต์โดยตรง
สำหรับข้อความในภาษาที่ยังไม่ได้พัฒนา จะใช้ภาษาอังกฤษเป็นตัวแทน
หมายเหตุ: ตั้งแต่ v0.11.0 เป็นต้นไป จะเลิกใช้โมดูล pyglet อย่างสมบูรณ์ และจะใช้วิธีใหม่ในการเปลี่ยนฟอนต์ของอินเทอร์เฟซเพื่อลดความซับซ้อนของโปรแกรม
v0.10.0
เปลี่ยนตรรกะการตั้งค่าแบบอักษร
ปรับรูปแบบหมายเลขเวอร์ชันให้เป็น x.y.z
""",
    # 韩语
    """업데이트 로그(v0.10.0 이상)
v0.14.2
API 응답 코드 처리를 통일하고 오류와 시간 초과를 처리합니다.
여러 API 경로를 수정하고 댓글 페이지를 지원합니다. 창을 닫으면 팬 수 모니터링이 중지됩니다.
v0.14.1
로그인 QR 코드를 앱에 표시하고 로그인 상태를 기기에 저장할 수 있습니다.
사용자 조회 응답 처리와 오류 및 누락 필드 처리를 수정했습니다.
v0.14.0
v0.13.1을 기반으로 업데이트 계속
고 DPI 지원 추가: 시스템 DPI 배율을 읽어 인터페이스, 글꼴, 구성 요소 간격을 자동으로 확대·축소하므로 고해상도 화면에서 더 이상 흐릿하지 않습니다
시작할 때 시스템 언어를 자동으로 읽어 인터페이스 언어를 전환하며, 언어 번호를 입력하라는 창이 더 이상 표시되지 않습니다
initialize.txt는 이제 초기 글꼴 설정에만 사용되며, 파일의 언어 번호는 더 이상 적용되지 않습니다
나머지 12개 언어의 업데이트 로그를 보완했습니다(그동안 v0.12.0~v0.13.1이 누락됨)
스페인어와 인도네시아어에서 업데이트 로그가 강제로 영어로 표시되던 문제를 수정
13개 언어의 인터페이스 텍스트를 전면 검토·보완하고, 오역과 영어 임시 문구를 수정하며, 텍스트 항목 누락으로 인한 비정상 종료를 수정
v0.13.1
최종 버전, 업데이트 중단
v0.13.0
더 많은 기능이 번체 중국어 OpenCC 자동 변환을 지원
최신 Python 환경에서 간체/번체 변환기를 열 수 없는 버그를 수정했으나, 이 기능은 여전히 정상적으로 변환되지 않습니다(출력 텍스트가 입력 텍스트와 완전히 동일).
사용자 지정 글꼴을 변경할 때 취소를 누르면 화면이 기본 SimSun 글꼴로 돌아가는 버그를 수정
종료 확인 창과 글꼴 변경 시 잘못된 숫자를 입력했을 때의 경고 창을 추가
v0.12.0
일부 텍스트 수정
코드를 정리하여 가독성을 높임
Bilibili API의 오류를 던지는 테스트를 시작
대부분의 구성 요소를 "requirements" 폴더로 이동(initialize.txt는 선택 구성 요소이므로 이동하지 않음)
참고:
1. 텍스트 정리로 인해 "로그인 사용자 정보"의 다국어 텍스트 대부분이 제거되고 영어로 대체되었으며, 추후 복원할 예정입니다.
2. 다음 버전에서는 1.0.0 객체 지향 프로그램으로 바로 전환할 예정이며, 이전 버전과 호환되지 않습니다.
v0.11.1
일부 기능 코드를 병합하여 프로그램 크기를 줄임
사용자가 팔로우한 사용자 목록과 팬 목록을 조회하는 기능 추가(로그인이 필요하므로 "로그인 사용자 작업" 기능 아래에 배치됨)
일본어 모드에서 "기타 도구" 창을 열 때 버튼이 없고 오류가 발생하는 문제를 수정
UP의 동영상 상태 조회에 전자기력 데이터를 추가
참고: v1.0.0은 프로그램을 완전히 객체 지향으로 전환하고 더 오픈 소스로 만들 것입니다
v0.11.0
OpenCC 모듈을 사용하여 번체 중국어로의 텍스트 변환을 구현하여 번체 중국어 모드의 적용 범위를 더욱 포괄적으로 만듦(OpenCC 프로젝트 주소: https://github.com/BYVoid/OpenCC)
pyglet 모듈에 대한 요구 사항을 취소.
프로그램 종료 시 사용자 팬 수 실시간 데이터 상자를 닫을 수 없고 응답하지 않는 문제를 수정
일부 번체 중국어 텍스트 수정
각 기능의 다국어 지원을 일정 부분 계속 개선
네트워크가 불안정하여 요청이 실패하면 성공하거나 100번 실패할 때까지 다시 시도하도록 변경
v0.10.1
수동 크기 조정으로 인한 레이아웃 문제를 방지하기 위해 창 크기를 고정
업데이트 로그를 새로 구성
버튼 텍스트와 "정보" 인터페이스의 텍스트 처리 최적화
구성 요소를 직접 실행하면 안내 메시지가 표시됨
아직 개발되지 않은 언어의 텍스트에는 영어를 자리 표시자로 사용
참고: v0.11.0부터 pyglet 모듈은 완전히 폐기되고 프로그램 복잡성을 줄이기 위해 인터페이스 글꼴을 변경하는 새로운 방법이 채택됩니다
v0.10.0
글꼴 설정 로직 변경
버전 번호를 x.y.z 형식으로 정규화
""",
    # 俄语
    """Журнал обновлений (v0.10.0 и новее)
v0.14.2
Унифицирована обработка кодов API, ошибок и тайм-аутов.
Исправлены несколько API-адресов. Комментарии загружаются по страницам, а мониторинг подписчиков прекращается при закрытии окна.
v0.14.1
QR-код входа отображается в приложении. Вход можно сохранить на устройстве.
Исправлена обработка карточек пользователей, ошибок и отсутствующих полей.
v0.14.0
Продолжение разработки на основе v0.13.1
Добавлена поддержка экранов с высоким DPI: программа считывает масштаб системы и автоматически масштабирует интерфейс, шрифты и отступы, поэтому на экранах высокой плотности больше нет размытия
Язык интерфейса теперь автоматически определяется по системному языку при запуске; окно с запросом номера языка больше не появляется
initialize.txt теперь служит только для настройки начального шрифта; номер языка в нём больше не используется
Дополнены журналы обновлений остальных 12 языков (ранее отсутствовали записи с v0.12.0 по v0.13.1)
Исправлена ошибка, из-за которой журнал обновлений принудительно отображался на английском в испанском и индонезийском
Проведена проверка и дополнение текстов интерфейса на всех 13 языках, исправлены ошибки перевода и английские заглушки, устранены сбои из-за отсутствующих текстовых записей
v0.13.1
Финальная версия, разработка прекращена
v0.13.0
Больше функций поддерживают автоматическое преобразование в традиционный китайский через OpenCC
Исправлена ошибка, из-за которой конвертер упрощённого/традиционного китайского не открывался в последней версии Python; однако преобразование по-прежнему работает некорректно (выходной текст полностью совпадает с введённым)
Исправлена ошибка, из-за которой интерфейс возвращался к шрифту SimSun по умолчанию после нажатия «Отмена» при смене пользовательского шрифта
Добавлены окно подтверждения выхода и предупреждение при вводе недопустимого числа при смене шрифта
v0.12.0
Исправлены некоторые тексты
Код отформатирован для большей читаемости
Начато тестирование вывода ошибок API Bilibili
Большинство компонентов перенесено в папку «requirements» (initialize.txt не перенесён, так как является необязательным)
Примечание:
1. Из-за правки текстов большинство многоязычных текстов в разделе «Информация о вошедшем пользователе» удалено и заменено английским; позже они будут восстановлены.
2. Следующая версия, как ожидается, сразу перейдёт к объектно-ориентированной программе 1.0.0, несовместимой со старыми версиями.
v0.11.1
Некоторые функциональные коды объединены для уменьшения размера программы
Добавлена функция запроса списка подписок и списка фанатов пользователя (требуется вход, поэтому размещена в функции «Операции вошедшего пользователя»)
Исправлена ошибка, при которой окно «Другие инструменты» открывалось в японском режиме без кнопок и с сообщением об ошибке
В запрос статуса видео UP добавлены данные об электромагнитной силе
Примечание: v1.0.0 сделает программу полностью объектно-ориентированной и более открытой
v0.11.0
Использование модуля OpenCC для преобразования текста в традиционный китайский, что делает охват традиционного китайского режима более полным (адрес проекта OpenCC: https://github.com/BYVoid/OpenCC)
Отказ от требования к модулю pyglet.
Исправлена ошибка, из-за которой окно данных о числе фанатов в реальном времени не закрывалось и не отвечало при выходе из программы
Исправлены некоторые тексты на традиционном китайском
Многоязычная поддержка различных функций продолжена
При нестабильной сети неудачные запросы повторяются до 100 раз
v0.10.1
Размер окна зафиксирован, чтобы избежать проблем с макетом при ручном изменении
Журнал обновлений переработан
Оптимизирована обработка текста кнопок и интерфейса «О программе»
При прямом запуске компонента теперь выводится предупреждение
Для текстов на неразработанных языках используется английский как заполнитель
Примечание: начиная с v0.11.0 модуль pyglet будет полностью заброшен и будет применён новый способ изменения шрифта интерфейса для снижения сложности программы
v0.10.0
Изменена логика настройки шрифтов
Номера версий приведены к формату x.y.z
""",
    # 越南语
    """Nhật ký cập nhật (v0.10.0 trở lên)
v0.14.2
Thống nhất cách đọc mã phản hồi API và xử lý lỗi hoặc hết thời gian chờ.
Sửa một số API, phân trang bình luận và dừng theo dõi người hâm mộ khi đóng cửa sổ.
v0.14.1
Hiển thị mã QR đăng nhập trong ứng dụng và cho phép lưu phiên đăng nhập trên thiết bị.
Sửa tra cứu người dùng và xử lý lỗi hoặc trường dữ liệu bị thiếu.
v0.14.0
Tiếp tục cập nhật dựa trên v0.13.1
Thêm hỗ trợ màn hình độ phân giải cao (High DPI): chương trình đọc tỉ lệ DPI của hệ thống và tự động phóng to/thu nhỏ giao diện, phông chữ và khoảng cách các thành phần, nên không còn bị mờ trên màn hình độ phân giải cao
Ở lần khởi động, chương trình tự động đọc ngôn ngữ hệ thống và chuyển ngôn ngữ giao diện; không còn hộp thoại yêu cầu nhập số hiệu ngôn ngữ
initialize.txt nay chỉ dùng để đặt phông chữ ban đầu; số hiệu ngôn ngữ trong tệp không còn hiệu lực
Bổ sung nhật ký cập nhật của 12 ngôn ngữ còn lại (trước đây thiếu v0.12.0 đến v0.13.1)
Sửa lỗi nhật ký cập nhật bị buộc hiển thị bằng tiếng Anh ở tiếng Tây Ban Nha và tiếng Indonesia
Rà soát và bổ sung toàn bộ văn bản giao diện cho 13 ngôn ngữ, sửa lỗi dịch và các đoạn tiếng Anh thay thế, đồng thời khắc phục lỗi thoát do thiếu mục văn bản
v0.13.1
Bản cuối cùng, ngừng phát triển
v0.13.0
Nhiều chức năng hơn hỗ trợ chuyển tự động sang tiếng Trung phồn thể bằng OpenCC
Đã sửa lỗi không thể mở công cụ chuyển đổi giản thể/phồn thể trên môi trường Python mới nhất, nhưng chức năng này hiện vẫn chưa chuyển đổi chính xác (văn bản đầu ra giống hệt văn bản đầu vào)
Đã sửa lỗi giao diện quay về phông chữ SimSun mặc định sau khi bấm Hủy khi thay đổi phông chữ tùy chỉnh
Đã thêm hộp thoại xác nhận thoát và hộp thoại cảnh báo khi nhập số không hợp lệ lúc thay đổi phông chữ
v0.12.0
Sửa một số nội dung văn bản
Định dạng lại mã nguồn để dễ đọc hơn
Bắt đầu thử nghiệm việc đưa ra lỗi từ API của Bilibili
Chuyển hầu hết các thành phần vào thư mục "requirements" (initialize.txt không được chuyển vì là thành phần tùy chọn)
Lưu ý:
1. Do việc chỉnh lý văn bản, phần lớn văn bản đa ngôn ngữ trong "Thông tin người dùng đã đăng nhập" đã bị loại bỏ và thay bằng tiếng Anh, sẽ được bổ sung lại sau.
2. Phiên bản tiếp theo dự kiến sẽ chuyển thẳng sang chương trình hướng đối tượng 1.0.0, không tương thích với phiên bản cũ.
v0.11.1
Hợp nhất một số mã chức năng để giảm kích thước chương trình
Đã thêm chức năng truy vấn danh sách người dùng được theo dõi và danh sách người hâm mộ của một người dùng (yêu cầu đăng nhập, do đó được đặt trong chức năng "Thao tác của người dùng đã đăng nhập")
Đã khắc phục sự cố cửa sổ "Công cụ khác" mở ra không có nút và báo lỗi ở chế độ tiếng Nhật
Đã thêm dữ liệu lực điện từ vào truy vấn trạng thái video của UP
Lưu ý: v1.0.0 sẽ chuyển chương trình hoàn toàn sang hướng đối tượng và mã nguồn mở hơn
v0.11.0
Sử dụng mô-đun OpenCC để chuyển văn bản sang tiếng Trung phồn thể, giúp chế độ tiếng Trung phồn thể được bao phủ toàn diện hơn (địa chỉ dự án OpenCC: https://github.com/BYVoid/OpenCC)
Hủy bỏ yêu cầu đối với mô-đun pyglet.
Đã khắc phục sự cố hộp dữ liệu thời gian thực về số người hâm mộ không thể đóng và bị treo khi thoát chương trình
Sửa một số văn bản tiếng Trung phồn thể
Tiếp tục cải thiện hỗ trợ đa ngôn ngữ cho từng chức năng
Khi mạng không ổn định và yêu cầu thất bại, chương trình sẽ thử lại cho đến khi thành công hoặc thất bại 100 lần
v0.10.1
Khóa kích thước cửa sổ để tránh các vấn đề bố cục do thay đổi thủ công
Thiết kế lại nhật ký cập nhật
Tối ưu hóa cách xử lý văn bản của các nút và giao diện "Giới thiệu"
Hiển thị lời nhắc khi cố chạy trực tiếp một thành phần
Đối với văn bản bằng các ngôn ngữ chưa phát triển, tiếng Anh được dùng làm trình giữ chỗ
Lưu ý: Bắt đầu từ v0.11.0, mô-đun pyglet sẽ bị loại bỏ hoàn toàn và một cách mới để thay đổi phông chữ giao diện sẽ được áp dụng để giảm độ phức tạp của chương trình
v0.10.0
Thay đổi logic cài đặt phông chữ
Chuẩn hóa số phiên bản sang định dạng x.y.z
""",
    # 葡萄牙语
    """Registros de atualização (v0.10.0 e posteriores)
v0.14.2
Os códigos de resposta da API são tratados de forma uniforme, incluindo erros e tempos limite.
Foram corrigidos vários endpoints. Os comentários são paginados e a monitorização dos seguidores termina ao fechar a janela.
v0.14.1
O código QR de início de sessão é apresentado na aplicação. É possível guardar a sessão no dispositivo.
Corrigida a consulta de utilizadores e o tratamento de erros e campos em falta.
v0.14.0
Continuidade do desenvolvimento com base na v0.13.1
Adicionado suporte a telas de alto DPI: o programa lê a escala de DPI do sistema e ajusta automaticamente a interface, as fontes e os espaçamentos, que deixam de ficar desfocados em telas de alta resolução
O idioma da interface agora é detectado automaticamente a partir do idioma do sistema na inicialização; a caixa de diálogo que pedia um número de idioma não aparece mais
O initialize.txt agora serve apenas para definir a fonte inicial; o número de idioma nele não é mais utilizado
Completados os registros de atualização dos outros 12 idiomas (faltavam de v0.12.0 a v0.13.1)
Corrigido o registro de atualização que era exibido à força em inglês em espanhol e indonésio
Revisão e preenchimento dos textos da interface em todos os 13 idiomas, correção de traduções erradas e de textos provisórios em inglês, e correção de falhas causadas por entradas de texto em falta
v0.13.1
Versão final, desenvolvimento encerrado
v0.13.0
Mais funcionalidades agora oferecem suporte à conversão automática para chinês tradicional via OpenCC
Corrigido o bug que impedia abrir o conversor simplificado/tradicional na versão mais recente do Python; porém, a conversão ainda não funciona corretamente (o texto de saída é idêntico ao texto digitado)
Corrigido o bug em que a interface voltava para a fonte SimSun padrão após clicar em Cancelar ao alterar a fonte personalizada
Adicionadas a janela de confirmação de saída e a janela de aviso para números inválidos ao alterar a fonte
v0.12.0
Correção de alguns textos
Código reformatado para melhor legibilidade
Início dos testes de lançamento de erros da API do Bilibili
A maioria dos componentes foi movida para a pasta "requirements" (initialize.txt não foi movido por ser opcional)
Nota:
1. Devido à revisão dos textos, a maior parte dos textos multilíngues em "Informações do usuário conectado" foi removida e substituída por inglês; será restaurada posteriormente.
2. A próxima versão deverá passar diretamente para um programa orientado a objetos 1.0.0, incompatível com as versões antigas.
v0.11.1
Mesclagem de alguns códigos funcionais para reduzir o tamanho do programa
Adicionada a função de consultar os usuários seguidos e os fãs de um usuário (exige login, por isso fica na função "Operações do usuário conectado")
Corrigido o problema de a janela "Outras ferramentas" abrir sem botões e com mensagem de erro no modo japonês
Adicionados dados de força eletromagnética à consulta de status dos vídeos do UP
Nota: a v1.0.0 tornará o programa totalmente orientado a objetos e mais open-source
v0.11.0
Uso do módulo OpenCC para converter o texto em chinês tradicional, tornando a cobertura do modo chinês tradicional mais abrangente (endereço do projeto OpenCC: https://github.com/BYVoid/OpenCC)
Removida a exigência do módulo pyglet.
Corrigido o problema de a janela de dados em tempo real do número de fãs não poder ser fechada e ficar sem resposta ao sair do programa
Revisão de alguns textos em chinês tradicional
Aprimoramento contínuo do suporte multilíngue de cada função
Quando a rede está instável e a solicitação falha, ela é repetida até dar certo ou até 100 falhas
v0.10.1
Tamanho da janela bloqueado para evitar problemas de layout causados por redimensionamento manual
Registros de atualização redesenhados
Otimização do texto dos botões e da interface "Sobre"
Um aviso é exibido ao tentar executar um componente diretamente
Para textos em idiomas ainda não desenvolvidos, o inglês é usado como espaço reservado
Nota: a partir da v0.11.0, o módulo pyglet será completamente abandonado e uma nova forma de alterar a fonte da interface será adotada para reduzir a complexidade do programa
v0.10.0
Lógica de configuração de fonte alterada
Números de versão normalizados para o formato x.y.z
""",
    # 西班牙语
    """Registros de actualización (v0.10.0 y posteriores)
v0.14.2
Se unificó el tratamiento de los códigos de respuesta de la API, los errores y los tiempos de espera.
Se corrigieron varios endpoints, se paginaron los comentarios y el seguimiento de seguidores se detiene al cerrar la ventana.
v0.14.1
El código QR de inicio de sesión se muestra en la aplicación. Se puede guardar la sesión en el dispositivo.
Se corrigió la consulta de usuarios y el tratamiento de errores y campos ausentes.
v0.14.0
Continuidad del desarrollo sobre la v0.13.1
Añadida compatibilidad con pantallas de alto DPI: el programa lee la escala de DPI del sistema y ajusta automáticamente la interfaz, las fuentes y los espaciados, por lo que deja de verse borroso en pantallas de alta resolución
El idioma de la interfaz se detecta ahora automáticamente a partir del idioma del sistema al iniciarse; ya no aparece el cuadro de diálogo que pedía un número de idioma
initialize.txt ahora solo sirve para configurar la fuente inicial; el número de idioma que contiene ya no se utiliza
Completados los registros de actualización de los otros 12 idiomas (faltaban de la v0.12.0 a la v0.13.1)
Corregido el registro de actualización que se mostraba forzosamente en inglés en español e indonesio
Revisión y compleción de los textos de la interfaz en los 13 idiomas, corrección de traducciones erróneas y de textos provisionales en inglés, y corrección de fallos por entradas de texto ausentes
v0.13.1
Versión final, desarrollo detenido
v0.13.0
Más funciones admiten la conversión automática a chino tradicional mediante OpenCC
Corregido el error que impedía abrir el conversor simplificado/tradicional en la última versión de Python; sin embargo, la conversión sigue sin funcionar correctamente (el texto de salida es idéntico al texto introducido)
Corregido el error por el que la interfaz volvía a la fuente SimSun predeterminada tras pulsar Cancelar al cambiar la fuente personalizada
Añadidos el diálogo de confirmación de salida y el aviso al introducir un número no válido al cambiar la fuente
v0.12.0
Corrección de algunos textos
Código reformateado para mejorar su legibilidad
Inicio de las pruebas de lanzamiento de errores de la API de Bilibili
La mayoría de los componentes se han movido a la carpeta "requirements" (initialize.txt no se ha movido por ser opcional)
Nota:
1. Debido a la revisión de textos, se ha eliminado la mayor parte del texto multilingüe de "Información del usuario conectado" y se ha sustituido por inglés; se restaurará más adelante.
2. Está previsto que la próxima versión pase directamente a un programa orientado a objetos 1.0.0, incompatible con las versiones anteriores.
v0.11.1
Fusión de algunos códigos funcionales para reducir el tamaño del programa
Añadida la función de consultar los usuarios seguidos y los fans de un usuario (requiere iniciar sesión, por lo que se coloca en la función "Operaciones del usuario conectado")
Corregido el problema por el que la ventana "Otras herramientas" se abría sin botones y con un mensaje de error en modo japonés
Añadidos datos de fuerza electromagnética a la consulta del estado de los vídeos del UP
Nota: la v1.0.0 hará que el programa sea totalmente orientado a objetos y más de código abierto
v0.11.0
Uso del módulo OpenCC para convertir el texto a chino tradicional, lo que hace que la cobertura del modo chino tradicional sea más completa (dirección del proyecto OpenCC: https://github.com/BYVoid/OpenCC)
Se elimina el requisito del módulo pyglet.
Corregido el problema por el que la ventana de datos en tiempo real del número de fans no se podía cerrar y dejaba de responder al salir del programa
Revisión de algunos textos en chino tradicional
Mejora continua del soporte multilingüe de cada función
Cuando la red es inestable y falla una solicitud, esta se reintenta hasta tener éxito o acumular 100 fallos
v0.10.1
Tamaño de la ventana bloqueado para evitar problemas de diseño causados por cambios manuales
Registros de actualización rediseñados
Optimización del texto de los botones y de la interfaz "Acerca de"
Se muestra un aviso al intentar ejecutar un componente directamente
Para los textos en idiomas aún no desarrollados se utiliza el inglés como marcador de posición
Nota: a partir de la v0.11.0, el módulo pyglet se abandonará por completo y se adoptará una nueva forma de cambiar la fuente de la interfaz para reducir la complejidad del programa
v0.10.0
Cambio en la lógica de configuración de la fuente
Números de versión normalizados al formato x.y.z
""",
    # 印度尼西亚语
    """Log pembaruan (v0.10.0 dan yang lebih baru)
v0.14.2
Kode respons API kini diproses secara seragam, termasuk saat terjadi galat atau waktu tunggu habis.
Beberapa endpoint telah diperbaiki. Komentar dimuat per halaman dan pemantauan pengikut berhenti saat jendela ditutup.
v0.14.1
Kode QR masuk ditampilkan di aplikasi dan sesi dapat disimpan di perangkat.
Pencarian pengguna kini menangani respons, galat, dan kolom yang tidak tersedia.
v0.14.0
Melanjutkan pembaruan dari v0.13.1
Menambahkan dukungan layar DPI tinggi: program membaca skala DPI sistem dan menyesuaikan antarmuka, font, serta jarak antar komponen secara otomatis, sehingga tidak lagi buram di layar beresolusi tinggi
Bahasa antarmuka kini dideteksi otomatis dari bahasa sistem saat mulai; dialog yang meminta nomor bahasa tidak lagi muncul
initialize.txt kini hanya digunakan untuk mengatur font awal; nomor bahasa di dalamnya tidak lagi berlaku
Melengkapi log pembaruan 12 bahasa lainnya (sebelumnya v0.12.0 hingga v0.13.1 tidak ada)
Memperbaiki log pembaruan yang selalu ditampilkan dalam bahasa Inggris pada bahasa Spanyol dan Indonesia
Meninjau dan melengkapi teks antarmuka pada 13 bahasa, memperbaiki kesalahan terjemahan dan teks sementara berbahasa Inggris, serta memperbaiki crash akibat entri teks yang hilang
v0.13.1
Versi final, pengembangan dihentikan
v0.13.0
Lebih banyak fitur mendukung konversi otomatis ke bahasa Mandarin Tradisional melalui OpenCC
Memperbaiki bug yang membuat konverter Sederhana/Tradisional tidak dapat dibuka pada versi Python terbaru, tetapi konversi tersebut masih belum berfungsi dengan benar (teks keluaran sama persis dengan teks masukan)
Memperbaiki bug di mana antarmuka kembali ke font SimSun bawaan setelah mengklik Batal saat mengubah font khusus
Menambahkan dialog konfirmasi keluar dan dialog peringatan saat memasukkan angka tidak valid ketika mengubah font
v0.12.0
Memperbaiki sebagian teks
Memformat ulang kode agar lebih mudah dibaca
Mulai menguji pelemparan kesalahan dari API Bilibili
Memindahkan sebagian besar komponen ke folder "requirements" (initialize.txt tidak dipindahkan karena bersifat opsional)
Catatan:
1. Karena perbaikan teks, sebagian besar teks multibahasa di "Info pengguna yang login" dihapus dan diganti dengan bahasa Inggris; akan dipulihkan nanti.
2. Versi berikutnya diperkirakan akan langsung beralih ke program berorientasi objek 1.0.0, yang tidak kompatibel dengan versi lama.
v0.11.1
Menggabungkan sebagian kode fungsi untuk mengurangi ukuran program
Menambahkan fungsi untuk menanyakan daftar pengguna yang diikuti dan daftar penggemar seorang pengguna (memerlukan login, sehingga ditempatkan di fungsi "Operasi pengguna yang login")
Memperbaiki masalah jendela "Alat lain" yang terbuka tanpa tombol dan menampilkan kesalahan dalam mode Jepang
Menambahkan data gaya elektromagnetik pada kueri status video UP
Catatan: v1.0.0 akan sepenuhnya mengubah program menjadi berorientasi objek dan lebih open-source
v0.11.0
Menggunakan modul OpenCC untuk mengonversi teks ke bahasa Mandarin Tradisional, sehingga cakupan mode Mandarin Tradisional menjadi lebih menyeluruh (alamat proyek OpenCC: https://github.com/BYVoid/OpenCC)
Membatalkan persyaratan modul pyglet.
Memperbaiki masalah jendela data real-time jumlah penggemar yang tidak dapat ditutup dan tidak merespons saat keluar dari program
Merevisi sebagian teks bahasa Mandarin Tradisional
Terus meningkatkan dukungan multibahasa untuk setiap fungsi
Saat jaringan tidak stabil dan permintaan gagal, permintaan akan dicoba ulang hingga berhasil atau gagal 100 kali
v0.10.1
Ukuran jendela dikunci untuk mencegah masalah tata letak akibat perubahan ukuran secara manual
Log pembaruan didesain ulang
Mengoptimalkan penanganan teks tombol dan antarmuka "Tentang"
Menampilkan peringatan saat mencoba menjalankan komponen secara langsung
Untuk teks dalam bahasa yang belum dikembangkan, bahasa Inggris digunakan sebagai placeholder
Catatan: mulai v0.11.0, modul pyglet akan sepenuhnya ditinggalkan dan cara baru untuk mengubah font antarmuka akan diterapkan untuk mengurangi kompleksitas program
v0.10.0
Mengubah logika pengaturan font
Nomor versi dinormalisasi ke format x.y.z
""",
]
if __name__ == "__main__":
    import time

    print(
        '请运行名为“TH_Bilibili_Toolbox”的主程序，本页面将于5秒后关闭。\nPlease run the main program named "TH_Bilibili_Toolbox". This page will close in 5 seconds.'
    )
    time.sleep(5)
