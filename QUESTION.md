### **pytest运行参数**
pytest 是一个功能强大的 Python 测试框架，支持多种运行参数。下面是一些常用的 pytest 运行参数：
- `-v`：显示测试用例的详细信息，包括测试用例的名称和执行结果。
- `-q`：只显示测试用例的执行结果，不显示详细信息。
- `-k EXPRESSION`：只运行名称中包含指定表达式的测试用例。例如，`pytest -k "test_login"` 只会运行名称中包含 "test_login" 的测试用例。
- `-m MARKEXPR`：只运行带有指定标记的测试用例。例如，`pytest -m smoke` 只会运行带有 "@pytest.mark.smoke" 标记的测试用例。
- `-x`：遇到第一个测试用例失败时停止测试。
- `--maxfail=num`：当测试用例失败的数量达到指定值时停止测试。
- `--tb=style`：设置错误信息的显示格式。可选值包括 "long"（默认值，显示完整的错误信息）、"short"（只显示错误的第一行）、"line"（只显示错误的最后一行）和 "no"（不显示错误信息）。
- `--html=report.html`：生成 HTML 格式的测试报告。
- `--self-contained-html`：生成自包含的 HTML 格式的测试报告，所有的 CSS 和 JavaScript 代码都包含在一个 HTML 文件中，方便分享和查看。
除了上面列出的参数之外，pytest 还支持许多其他的参数，可以通过 `pytest --help` 命令查看完整的参数列表。


### **pytest的常用参数化**
pytest 是 Python 中一个流行的测试框架，它提供了多种参数化方式来简化测试代码的编写。下面是 pytest 实现参数化的几种方法及实例：

1. 使用 pytest.mark.parametrize 装饰器

pytest.mark.parametrize 装饰器可以用来为测试函数提供参数化数据，它接受一个参数名和一个参数值列表，每个参数值列表都是一个元组，包含了测试函数需要的参数。下面是一个示例：

```python
import pytest

@pytest.mark.parametrize("test_input,expected_output", [("3+5", 8), ("2+4", 6), ("6*9", 54)])
def test_eval(test_input, expected_output):
    assert eval(test_input) == expected_output
```

在这个示例中，我们定义了一个名为 test_eval 的测试函数，它有两个参数 test_input 和 expected_output，分别表示测试输入和期望输出。我们使用 pytest.mark.parametrize 装饰器为这个测试函数提供了三组参数化数据，分别是 "3+5" 和 8、"2+4" 和 6、"6*9" 和 54。pytest 会自动运行这个测试函数三次，每次使用一个参数化数据进行测试。

2. 使用 fixture 函数

fixture 函数可以用来为测试函数提供参数化数据，它可以返回一个参数值列表，pytest 会自动将这些参数值传递给测试函数。下面是一个示例：

```python
import pytest

@pytest.fixture(params=[("3+5", 8), ("2+4", 6), ("6*9", 54)])
def test_data(request):
    return request.param

def test_eval(test_data):
    test_input, expected_output = test_data
    assert eval(test_input) == expected_output
```

在这个示例中，我们定义了一个名为 test_data 的 fixture 函数，它返回一个参数值列表，包含了三组参数化数据。我们在测试函数 test_eval 中使用了这个 fixture 函数，pytest 会自动运行 test_eval 三次，每次传递一个参数化数据给 test_data 函数，然后将返回值传递给 test_eval 函数。

3. 使用 pytest_generate_tests 函数

pytest_generate_tests 函数可以用来生成参数化数据，它接受一个 metafunc 参数，可以用来访问测试函数的参数名和参数值。下面是一个示例：

```python
import pytest

def pytest_generate_tests(metafunc):
    if "test_data" in metafunc.fixturenames:
        metafunc.parametrize("test_data", [("3+5", 8), ("2+4", 6), ("6*9", 54)])

def test_eval(test_data):
    test_input, expected_output = test_data
    assert eval(test_input) == expected_output
```

在这个示例中，我们定义了一个名为 pytest_generate_tests 的函数，它使用 metafunc 参数来访问测试函数的参数名和参数值。如果测试函数包含了名为 test_data 的参数，pytest 会自动调用 pytest_generate_tests 函数来生成参数化数据。我们在 pytest_generate_tests 函数中使用了 pytest.parametrize 方法来为 test_data 参数提供了三组参数化数据，然后 pytest 会自动运行 test_eval 函数三次，每次传递一个参数化数据给 test_data 参数。



### **等待**
在 UI 自动化测试中，等待是非常重要的一步，因为页面元素的加载和响应时间是不可预测的。以下是几种常见的等待方法：

1. 强制等待：使用 time.sleep() 方法来暂停测试执行一段时间。这种方法的缺点是不够灵活，可能会浪费时间，也可能会导致测试失败。

2. 隐式等待：使用 driver.implicitly_wait() 方法来设置全局等待时间。这种方法会在查找元素时等待一段时间，直到元素出现或等待时间结束。这种方法的缺点是可能会导致测试执行时间过长。

3. 显式等待：使用 WebDriverWait 类来等待元素的出现或消失。这种方法可以设置等待时间和等待条件，直到条件满足或等待时间结束。这种方法比较灵活，可以根据需要设置等待时间和条件。

4. Fluent 等待：使用 expected_conditions 类来等待元素的出现或消失。这种方法可以设置等待时间和等待条件，直到条件满足或等待时间结束。这种方法比较灵活，可以根据需要设置等待时间和条件。

需要注意的是，不同的等待方法适用于不同的场景，需要根据具体情况进行选择。在实际应用中，通常会结合多种等待方法来实现更加稳定和可靠的测试。

在 UI 自动化测试中，显示等待是一种常用的技术。它可以帮助我们等待某个条件在一定时间内变为真，然后再执行下一步操作。常见的等待条件包括元素可见、元素可点击、元素存在等等。
在 Selenium 中，可以使用 WebDriverWait 类来实现显示等待。具体实现方法如下：
```python
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# 等待元素可见
wait = WebDriverWait(driver, 10)
element = wait.until(EC.visibility_of_element_located((By.ID, 'element_id')))

# 等待元素可点击
wait = WebDriverWait(driver, 10)
element = wait.until(EC.element_to_be_clickable((By.ID, 'element_id')))

# 等待元素存在
wait = WebDriverWait(driver, 10)
element = wait.until(EC.presence_of_element_located((By.ID, 'element_id')))
```
在上面的代码中，我们首先导入了 WebDriverWait 类和一些常用的等待条件。然后，我们创建了一个 WebDriverWait 对象，并指定了最长等待时间。接着，我们使用 until() 方法来指定等待条件，直到条件成立或者超时为止。最后，我们可以通过返回的元素对象来执行后续的操作。
需要注意的是，显示等待应该尽量避免设置过长的等待时间，否则会影响测试效率。同时，如果等待时间设置过短，可能会导致测试失败。因此，需要根据具体情况来合理设置等待时间。


### **pytest常用断言方式**

pytest 中常用的断言方式是使用 `assert` 语句。下面是一些示例：

1. 检查相等关系：

   ```python
   assert 1 + 1 == 2
   assert "hello" + " " + "world" == "hello world"
   ```

2. 检查不等关系：

   ```python
   assert 1 != 2
   assert "hello" != "world"
   ```

3. 检查包含关系：

   ```python
   assert "hello" in "hello world"
   assert 1 in [1, 2, 3]
   ```

4. 检查异常：

   ```python
   def test_exception():
       with pytest.raises(ValueError):
           int("invalid")
   ```

在 pytest 中，如果断言失败，pytest 会输出详细的错误信息，帮助我们快速定位问题。

### **githubpush失败**
![img.png](img.png)


### **python的目录操作**
在 Python 中，可以使用 `os` 模块进行目录操作。以下是一些常用的目录操作函数：

1. `os.chdir(path)`：切换当前工作目录到指定路径 `path`。
2. `os.getcwd()`：获取当前工作目录。
3. `os.listdir(path)`：返回指定路径 `path` 下的所有文件和目录的名称列表。
4. `os.mkdir(path)`：创建一个新目录，目录名为 `path`。
5. `os.makedirs(path)`：递归地创建新目录，包括所有必需但不存在的中间目录。
6. `os.rmdir(path)`：删除指定目录，目录必须为空。
7. `os.removedirs(path)`：递归地删除指定目录及其所有子目录，目录必须为空。
8. `os.path.join(path1[, path2[, ...]])`：将多个路径组合成一个路径。

以下是一些示例代码：

```python
import os

# 切换当前工作目录到指定路径
os.chdir('/path/to/directory')

# 获取当前工作目录
current_dir = os.getcwd()

# 返回指定路径下的所有文件和目录的名称列表
dir_contents = os.listdir('/path/to/directory')

# 创建一个新目录
os.mkdir('/path/to/new_directory')

# 递归地创建新目录
os.makedirs('/path/to/new/directory')

# 删除指定目录
os.rmdir('/path/to/directory_to_delete')

# 递归地删除指定目录及其所有子目录
os.removedirs('/path/to/directory_to_delete')

# 将多个路径组合成一个路径
path = os.path.join('/path/to', 'directory', 'file.txt')
```
注意，在 Windows 系统中，路径分隔符为反斜杠 `\`，而在 Linux 和 macOS 系统中，路径分隔符为正斜杠 `/`。为了保证跨平台兼容性，建议使用 `os.path.join()` 函数来拼接路径。





### **python的excel文件的基础操作**
在 Python 中处理 .xls 和 .xlsx 文件，可以使用不同的库。其中，处理 .xls 文件，可以使用 xlrd 库，处理 .xlsx 文件，可以使用 openpyxl 或者 xlsxwriter 库。

使用 xlrd 库处理 .xls 文件，可以读取 Excel 文件中的数据，例如：

```python
import xlrd

# 打开 Excel 文件
workbook = xlrd.open_workbook('example.xls')

# 获取工作表
worksheet = workbook.sheet_by_index(0)

# 读取单元格数据
cell_value = worksheet.cell_value(0, 0)
```

使用 openpyxl 库处理 .xlsx 文件，可以读取、修改和创建 Excel 文件，例如：

```python
import openpyxl

# 打开 Excel 文件
workbook = openpyxl.load_workbook('example.xlsx')

# 获取工作表
worksheet = workbook.active

# 读取单元格数据
cell_value = worksheet.cell(row=1, column=1).value

# 修改单元格数据
worksheet.cell(row=1, column=1).value = 'New Value'

# 保存 Excel 文件
workbook.save('example.xlsx')
```

使用 xlsxwriter 库处理 .xlsx 文件，可以创建和写入 Excel 文件，例如：

```python
import xlsxwriter

# 创建 Excel 文件
workbook = xlsxwriter.Workbook('example.xlsx')

# 创建工作表
worksheet = workbook.add_worksheet()

# 写入单元格数据
worksheet.write(0, 0, 'Hello World!')

# 保存 Excel 文件
workbook.close()
```

需要注意的是，xlrd 和 openpyxl 都支持读取 .xlsx 文件，但是 xlrd 不支持写入 .xlsx 文件。因此，如果需要写入 .xlsx 文件，建议使用 openpyxl 或者 xlsxwriter 库。


### **对于验证码的简单操作**
对于验证码验证登录的测试，我们可以使用 pytest 和 Selenium 来实现。下面是一个示例：
```python
import pytest
from selenium import webdriver

def test_login_with_valid_code():
    # 打开浏览器
    driver = webdriver.Chrome()
    driver.get("https://example.com/login")

    # 输入用户名和密码
    username_input = driver.find_element_by_name("username")
    password_input = driver.find_element_by_name("password")
    username_input.send_keys("user")
    password_input.send_keys("pass")

    # 获取验证码
    code_img = driver.find_element_by_css_selector(".code-img")
    code = code_img.text

    # 输入验证码
    code_input = driver.find_element_by_name("code")
    code_input.send_keys(code)

    # 点击登录按钮
    login_button = driver.find_element_by_css_selector(".login-btn")
    login_button.click()

    # 验证登录成功
    assert driver.current_url == "https://example.com/home"

    # 关闭浏览器
    driver.quit()

def test_login_with_invalid_code():
    # 打开浏览器
    driver = webdriver.Chrome()
    driver.get("https://example.com/login")

    # 输入用户名和密码
    username_input = driver.find_element_by_name("username")
    password_input = driver.find_element_by_name("password")
    username_input.send_keys("user")
    password_input.send_keys("pass")

    # 输入错误的验证码
    code_input = driver.find_element_by_name("code")
    code_input.send_keys("invalid")

    # 点击登录按钮
    login_button = driver.find_element_by_css_selector(".login-btn")
    login_button.click()

    # 验证登录失败
    assert "验证码错误" in driver.page_source

    # 关闭浏览器
    driver.quit()
```

在这个示例中，我们定义了两个测试函数，分别测试了使用有效验证码和无效验证码登录的情况。在每个测试函数中，我们使用 Selenium 打开浏览器，输入用户名、密码和验证码，然后点击登录按钮。最后，我们使用 `assert` 语句验证登录结果是否符合预期。如果登录成功，我们验证当前页面的 URL 是否是首页的 URL；如果登录失败，我们验证页面是否包含错误提示信息。在每个测试函数结束后，我们使用 `driver.quit()` 关闭浏览器。


### **无头配置**
要在 pytest 中使用无头浏览器进行测试，你需要使用 Selenium WebDriver。Selenium WebDriver 是一个用于自动化 Web 应用程序测试的工具，它可以与各种浏览器进行交互并模拟用户操作。

在使用 Selenium WebDriver 之前，你需要先安装一个浏览器驱动程序。例如，如果你要使用 Chrome 浏览器进行测试，你需要下载 ChromeDriver 并将其添加到系统路径中。你可以在以下链接中下载 ChromeDriver：

https://sites.google.com/a/chromium.org/chromedriver/downloads

安装好 ChromeDriver 后，你可以使用 Selenium WebDriver 的 Python 接口来编写测试用例。下面是一个使用无头 Chrome 浏览器进行测试的示例：

```python
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest

@pytest.fixture(scope='session')
def browser():
    # 设置 Chrome 为无头模式
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    # 启动 Chrome 浏览器
    driver = webdriver.Chrome(options=chrome_options)
    yield driver
    # 关闭浏览器
    driver.quit()

def test_example(browser):
    # 打开网页
    browser.get('https://www.google.com')
    # 获取页面标题
    assert 'Google' in browser.title
```

在这个示例中，我们使用了 pytest 的 fixture 功能来创建一个浏览器实例。我们使用了 ChromeOptions 类来设置 Chrome 为无头模式，并使用 webdriver.Chrome() 方法来启动 Chrome 浏览器。在测试用例中，我们使用了 browser.get() 方法来打开一个网页，并使用 assert 语句来检查页面标题是否包含 'Google'。最后，我们使用 yield 关键字来返回浏览器实例，并在测试结束后使用 driver.quit() 方法来关闭浏览器。

这是一个简单的示例，你可以根据你的具体需求进行修改和扩展。

可以使用 `pytest-xvfb` 插件来实现无头浏览器的配置。这个插件可以在 Linux 上使用虚拟 X 窗口来运行浏览器，从而实现无头模式的测试。安装方法如下：

```
pip install pytest-xvfb
```

然后在 `pytest.ini` 文件中添加以下内容：

```
[pytest]
addopts = --xvfb
```

这样就可以在运行 pytest 时自动启动虚拟 X 窗口，并在其中运行浏览器了。