PyQtPractice
============

PyQt(QtのPython向けbinding)を使って遊ぶ

「PyQtではじめるGUIプログラミング」<http://www.slideshare.net/RansuiIso/pyqtgui>をチュートリアルにする

* HelloWorld/
* RamenTimer/

上記が終わったので<http://zetcode.com/gui/pyqt4/>をやってみる

* ZetCodeTutorial/


環境構築
--------

1. 環境はmac OSX 10.9(Mavericks)なHomebrewでIDEはPyCharm 3 CE

2. python3をインストール

	```
	% brew install python3 --framework
	```

3. sip、qt、pyqtをpython3で使えるオプション付けてインストール

	```
	% brew install sip --with-python3
	% brew install qt
	% brew install pyqt --with-python3
	```

4. PyCharmにInterpreterを設定する

	`Preferences`→`Project Interpreter`→`Python Interpreters`で
	`+`ボタンより2でインストールしたPython3を選択する  
	設定が完了したらプロジェクトのインタープリターとして設定するかどうかを聞かれるので`Yes`を選択する

5. Qtのツールへのシンボリックリンクをはる(おこのみで)

    ```
    # qtのインストールディレクトリの各種appを/Applicationsに
    % mkdir /Applications/Qt
    % ln -s /usr/local/Cellar/qt/<version>/<Application>.app/ /Applications/Qt/<Application>.app
    ```

