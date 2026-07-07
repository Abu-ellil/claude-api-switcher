# ⚡ Claude Code API Switcher

[English](#english) | [العربية](#arabic)

---

<a name="english"></a>
## English

A beautiful modern GUI application to instantly switch between different API providers for Claude Code. Switch between Z.AI, LM Studio, Ollama, Anthropic Official, or add your own custom providers with ease.

### ✨ Features

- **Modern Dark Theme UI** - Beautiful, user-friendly interface built with CustomTkinter
- **Auto-Detection** - Automatically finds your Claude Code settings file
- **Quick Switching** - Switch between providers with one click
- **Custom Providers** - Add your own API providers
- **Persistent Storage** - Your custom providers are saved for future use
- **Cross-Platform** - Works on Windows, macOS, and Linux

### 📸 Pre-configured Providers

| Provider | URL | Description |
|----------|-----|-------------|
| Z.AI API | `https://api.z.ai/api/anthropic` | Z.AI Configuration |
| LM Studio | `http://localhost:1234/v1` | Local Server (Port 1234) |
| Ollama | `http://localhost:11434/v1` | Local Server (Port 11434) |
| Anthropic Official | Default | Default API Endpoint |

### 📋 Requirements

- Python 3.8 or higher
- CustomTkinter (optional, for modern UI)

### 🚀 Installation

#### Option 1: Run from Source

```bash
# Clone the repository
git clone https://github.com/yourusername/claude-api-switcher.git
cd claude-api-switcher

# Install dependencies
pip install -r requirements.txt

# Run the application
python app.py
```

#### Option 2: Run the Batch File (Windows)

Simply double-click `run.bat` to launch the application.

```batch
@echo off
python app.py
pause
```

### 🔨 Building an Executable

To build a standalone executable:

```bash
# Build the executable
pyinstaller --onefile --windowed --name "Claude-API-Switcher" app.py

# Or use the build script
build.bat
```

The executable will be created in the `dist` folder.

### 📖 Usage

1. **Launch the Application**
   - Run `python app.py` or double-click `run.bat`

2. **Settings File**
   - The app auto-detects your Claude Code settings file
   - Or click "Browse" to manually select `settings.json`

3. **Select a Provider**
   - Choose from pre-configured providers or your custom ones
   - Click "Apply Changes"

4. **Restart Claude Code**
   - Restart Claude Code for the changes to take effect

### ➕ Adding Custom Providers

1. Click the "Custom Provider" section
2. Enter:
   - **Name**: Provider name (e.g., "My Custom API")
   - **URL**: API endpoint (e.g., `https://api.example.com/v1`)
   - **Description**: Optional description
3. Click "Add Provider"

### 📁 Settings File Locations

The app looks for `settings.json` in these locations:

- **Windows**: `%LOCALAPPDATA%\claude\settings.json`
- **macOS**: `~/.config/claude/settings.json`
- **Linux**: `~/.config/claude/settings.json`
- **Fallback**: `~/.claude/settings.json`

### 🛠️ Troubleshooting

**Settings file not found?**
- Click "Browse" and manually navigate to your Claude Code settings directory
- Make sure Claude Code has been run at least once to create the settings file

**Changes not applying?**
- Make sure to restart Claude Code after applying changes
- Verify the settings file path is correct

### ⚠️ "Dangerous Download Blocked" Warning

When downloading the `.exe` file, you may see a "Dangerous Download Blocked" warning. This is normal for unsigned executables. To proceed:

#### Chrome/Edge:
1. Click "Keep anyway" or "Allow download"
2. Or go to Downloads → click "Keep" on the blocked file

#### Windows Defender:
1. Click "More info"
2. Click "Run anyway"

#### Why this happens?
- The executable is not digitally signed (code signing certificates are expensive)
- The source code is public on GitHub for verification
- You can also build from source if you prefer

#### Safer Alternative:
Build from source code:
```bash
git clone https://github.com/Abu-ellil/claude-api-switcher.git
cd claude-api-switcher
pip install -r requirements.txt
python app.py
```

### 📄 License

MIT License - feel free to use and modify as needed.

### 🤝 Contributing

Contributions are welcome! Feel free to submit issues and pull requests.

---

<a name="arabic"></a>
## العربية

تطبيق واجهة مستخدم حديث وجميل للتبديل الفوري بين مزودي API المختلفين لـ Claude Code. التبديل بين Z.AI و LM Studio و Ollama و Anthropic Official أو أضف مزودين مخصصين الخاصين بك بسهولة.

### ✨ المميزات

- **واجهة مستخدم حديثة بالوضع الداكن** - واجهة جميلة وسهلة الاستخدام مبنية بـ CustomTkinter
- **الكشف التلقائي** - يجد ملف إعدادات Claude Code تلقائياً
- **التبديل السريع** - التبديل بين المزودين بنقرة واحدة
- **مزودون مخصصون** - أضف مزودي API الخاصين بك
- **التخزين الدائم** - يتم حفظ المزودين المخصصين للاستخدام المستقبلي
- **عبر الأنظمة** - يعمل على Windows و macOS و Linux

### 📸 المزودون المُهيأون مسبقاً

| المزود | الرابط | الوصف |
|-------|-------|-------|
| Z.AI API | `https://api.z.ai/api/anthropic` | إعدادات Z.AI |
| LM Studio | `http://localhost:1234/v1` | خادم محلي (المنفذ 1234) |
| Ollama | `http://localhost:11434/v1` | خادم محلي (المنفذ 11434) |
| Anthropic Official | الافتراضي | نقطة النهاية الافتراضية |

### 📋 المتطلبات

- Python 3.8 أو أعلى
- CustomTkinter (اختياري، للواجهة الحديثة)

### 🚀 التثبيت

#### الخيار 1: التشغيل من المصدر

```bash
# استنسخ المستودع
git clone https://github.com/yourusername/claude-api-switcher.git
cd claude-api-switcher

# قم بتثبيت المتطلبات
pip install -r requirements.txt

# تشغيل التطبيق
python app.py
```

#### الخيار 2: تشغيل ملف Batch (Windows)

انقر مرتين على `run.bat` لتشغيل التطبيق.

```batch
@echo off
python app.py
pause
```

### 🔨 بناء ملف تنفيذي

لبناء ملف تنفيذي مستقل:

```bash
# بناء الملف التنفيذي
pyinstaller --onefile --windowed --name "Claude-API-Switcher" app.py

# أو استخدام سكريبت البناء
build.bat
```

سيتم إنشاء الملف التنفيذي في مجلد `dist`.

### 📖 الاستخدام

1. **تشغيل التطبيق**
   - قم بتشغيل `python app.py` أو انقر مرتين على `run.bat`

2. **ملف الإعدادات**
   - يكتشف التطبيق تلقائياً ملف إعدادات Claude Code
   - أو انقر على "Browse" لتحديد `settings.json` يدوياً

3. **اختيار مزود**
   - اختر من المزودين المهيئين مسبقاً أو المزودين المخصصين لك
   - انقر على "Apply Changes"

4. **إعادة تشغيل Claude Code**
   - أعد تشغيل Claude Code حتى تؤخذ التغييرات في الاعتبار

### ➕ إضافة مزودين مخصصين

1. انقر على قسم "Custom Provider"
2. أدخل:
   - **الاسم**: اسم المزود (مثلاً "My Custom API")
   - **الرابط**: نقطة نهاية API (مثلاً `https://api.example.com/v1`)
   - **الوصف**: وصف اختياري
3. انقر على "Add Provider"

### 📁 مواقع ملف الإعدادات

يبحث التطبيق عن `settings.json` في هذه المواقع:

- **Windows**: `%LOCALAPPDATA%\claude\settings.json`
- **macOS**: `~/.config/claude/settings.json`
- **Linux**: `~/.config/claude/settings.json`
- **البديل**: `~/.claude/settings.json`

### 🛠️ استكشاف الأخطاء وإصلاحها

**لم يتم العثور على ملف الإعدادات؟**
- انقر على "Browse" وانتقل يدوياً إلى مجلد إعدادات Claude Code
- تأكد من تشغيل Claude Code مرة واحدة على الأقل لإنشاء ملف الإعدادات

**التغييرات لا تطبق؟**
- تأكد من إعادة تشغيل Claude Code بعد تطبيق التغييرات
- تحقق من أن مسار ملف الإعدادات صحيح

### ⚠️ تحذير "Dangerous Download Blocked"

عند تحميل ملف `.exe`، قد تظهر رسالة "Dangerous Download Blocked". هذا طبيعي للملفات التنفيذية غير الموقعة. للتقدم:

#### Chrome/Edge:
1. انقر على "Keep anyway" أو "Allow download"
2. أو اذهب إلى Downloads → انقر "Keep" على الملف المحجوب

#### Windows Defender:
1. انقر على "More info"
2. انقر على "Run anyway"

#### لماذا يحدث هذا؟
- الملف التنفيذي غير موقّع رقمياً (شهادات التوقيع باهظة الثمن)
- الكود المصدري متاح للعامة على GitHub للتحقق
- يمكنك أيضاً البناء من المصدر إذا فضّلت

#### البديل الأآمن:
ابنِ من الكود المصدري:
```bash
git clone https://github.com/Abu-ellil/claude-api-switcher.git
cd claude-api-switcher
pip install -r requirements.txt
python app.py
```

### 📄 الترخيص

رخصة MIT - يمكنك استخدام وتعديل البرنامج حسب الحاجة.

### 🤝 المساهمة

المساهمات مرحب بها! لا تتردد في تقديم المشاكل وطلبات السحب.

---

<div align="center">

Made with ❤️ for the Claude Code community

</div>
