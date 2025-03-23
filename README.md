# dashboard-desktop-application

## ✨ Features
- 📂 **Load CSV File**: Users can select and open a CSV file.
- 🔍 **Search & Filter**: Search data within the loaded file.
- 📊 **View Data**: Display CSV content in a user-friendly table format.
- 📝 **Add New Data**: Insert new rows into the CSV.
- ✏️ **Edit Existing Data**: Modify existing rows.
- ❌ **Delete Rows**: Remove selected entries.
- 🔀 **Sort Data**: Click column headers to sort ascending/descending.
- 💾 **Save Changes**: Save modifications directly to the CSV file.
- 📦 **Standalone Application**: Runs as a desktop application without needing a code editor.

## 🚀 Setup & Installation
### Prerequisites
Ensure you have **Python 3.x** installed on your system. If not, download it from [Python.org](https://www.python.org/downloads/).

### 1️⃣ Install Dependencies
Navigate to the directory where `app.py` is located and install the required dependencies:
```bash
pip install pandas
```

### 2️⃣ Run the Application
Run the following command to launch the application:
```bash
python app.py
```

## 🖥️ Convert to Standalone Executable
To run the app **without Python**, create an executable using PyInstaller.

### **For Windows**:
#### 1️⃣ Install PyInstaller
```bash
pip install pyinstaller
```

#### 2️⃣ Create Executable
```bash
pyinstaller --onefile --windowed app.py
```

#### 3️⃣ Locate the Executable
The executable file (`app.exe`) will be inside the `dist` folder. You can now run it without needing Python installed.


### **For Linux**:
#### 1️⃣ Install PyInstaller
```bash
pip install pyinstaller
```

#### 2️⃣ Create Executable
```bash
pyinstaller --onefile --windowed app.py
```

#### 3️⃣ Run the Application
Execute the generated file in the `dist` folder:
```bash
./dist/app
```

If required, grant execution permissions:
```bash
chmod +x dist/app
```


Open `app.exe` file will be inside the `dist` folder.
