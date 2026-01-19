# Login Automata - DFA Implementation

## Proyek Mata Kuliah Teori Bahasa dan Automata

### 📚 Deskripsi Proyek

Proyek ini mengimplementasikan **Deterministic Finite Automaton (DFA)** untuk sistem autentikasi login sederhana.

### 🎯 Konsep DFA yang Diimplementasikan

#### State Diagram:

```
    username_benar      password_benar
q0 ----------------> q1 ----------------> q3 (ACCEPT)
 |                    |
 | username_salah     | password_salah
 |                    |
 v                    v
q2 (REJECT) <-------- q2
```

#### Komponen DFA:

- **Q (States)**: {q0, q1, q2, q3}

  - `q0`: State awal (belum ada input)
  - `q1`: Username valid
  - `q2`: State reject (login gagal)
  - `q3`: State accept (login berhasil)

- **Σ (Alphabet)**: {username_benar, username_salah, password_benar, password_salah}

- **δ (Transition Function)**:

  - δ(q0, username_benar) = q1
  - δ(q0, username_salah) = q2
  - δ(q1, password_benar) = q3
  - δ(q1, password_salah) = q2

- **q0**: Start state
- **F (Accept States)**: {q3}

### 📁 Struktur File

```
login_automata/
├── automata.py          # Implementasi class DFA
├── auth.py              # Aplikasi login menggunakan DFA
├── test_auth.py         # Test sederhana
├── test_automata.py     # Test suite lengkap dengan pytest
└── README.md            # Dokumentasi ini
```

### 🔧 Instalasi

1. **Install Python** (minimal versi 3.7)
2. **Install pytest**:

   ```bash
   pip install pytest
   ```

3. **Install pytest-cov** (optional, untuk coverage report):
   ```bash
   pip install pytest-cov
   ```

### 🚀 Cara Menjalankan Pytest

#### 1. Menjalankan Semua Test

```bash
pytest
```

#### 2. Menjalankan Test dengan Output Verbose

```bash
pytest -v
```

#### 3. Menjalankan Test dengan Detail Lengkap

```bash
pytest -v --tb=short
```

#### 4. Menjalankan Test Spesifik

```bash
# Test file tertentu
pytest test_automata.py

# Test class tertentu
pytest test_automata.py::TestLoginAutomata

# Test function tertentu
pytest test_automata.py::TestLoginAutomata::test_initial_state
```

#### 5. Menjalankan Test dengan Coverage Report

```bash
pytest --cov=. --cov-report=html
```

#### 6. Menjalankan Test dan Berhenti di Error Pertama

```bash
pytest -x
```

#### 7. Menjalankan Test dengan Output Print

```bash
pytest -v -s
```

### 📊 Contoh Output yang Diharapkan

```
================================ test session starts ================================
platform win32 -- Python 3.x.x, pytest-x.x.x
collected 20 items

test_automata.py::TestLoginAutomata::test_initial_state PASSED                [ 5%]
test_automata.py::TestLoginAutomata::test_transition_username_benar PASSED    [10%]
test_automata.py::TestLoginAutomata::test_transition_username_salah PASSED    [15%]
test_automata.py::TestLoginAutomata::test_transition_password_benar_from_q1 PASSED [20%]
test_automata.py::TestLoginAutomata::test_transition_password_salah_from_q1 PASSED [25%]
test_automata.py::TestLoginAutomata::test_full_path_to_accept_state PASSED    [30%]
test_automata.py::TestLoginAutomata::test_reject_state_username_salah PASSED  [35%]
test_automata.py::TestLoginAutomata::test_reject_state_password_salah PASSED  [40%]
test_automata.py::TestLoginFunction::test_login_berhasil PASSED               [45%]
test_automata.py::TestLoginFunction::test_login_username_salah PASSED         [50%]
test_automata.py::TestLoginFunction::test_login_password_salah PASSED         [55%]
test_automata.py::TestLoginFunction::test_login_username_password_salah PASSED [60%]
test_automata.py::TestLoginFunction::test_login_berbagai_input[...] PASSED    [65%]
...
test_automata.py::TestDFAProperties::test_accept_state_q3 PASSED              [95%]
test_automata.py::TestDFAProperties::test_reject_state_q2 PASSED             [100%]

================================ 20 passed in 0.05s =================================
```

### 🧪 Test Coverage

Test suite mencakup:

1. **Test Automata DFA**:

   - Initial state
   - Transisi antar state
   - Accept state (q3)
   - Reject state (q2)
   - Properti deterministik

2. **Test Fungsi Login**:

   - Login berhasil
   - Login gagal (username salah)
   - Login gagal (password salah)
   - Berbagai kombinasi input (parametrized test)

3. **Test Properti DFA**:
   - Deterministic property
   - State persistence
   - Accept/Reject states

### 💡 Cara Menggunakan

```python
from auth import login

# Login berhasil
result = login("admin", "12345")  # Returns: True

# Login gagal
result = login("user", "12345")   # Returns: False
result = login("admin", "wrong")  # Returns: False
```

### 📝 Catatan Penting

- Username valid: `admin`
- Password valid: `12345`
- DFA bersifat **deterministik**: setiap state + input menghasilkan tepat 1 state tujuan
- State `q3` adalah **accept state** (login berhasil)
- State `q2` adalah **reject state** (login gagal)

### 🎓 Konsep Automata yang Diterapkan

1. **Finite States**: Sistem memiliki jumlah state terbatas (4 states)
2. **Deterministic**: Tidak ada ambiguitas dalam transisi
3. **Transition Function**: Fungsi transisi yang jelas dan terdefinisi
4. **Accept State**: State akhir yang menandakan input diterima
5. **Reject State**: State yang menandakan input ditolak

### 📖 Referensi

- Teori Bahasa dan Automata
- Deterministic Finite Automaton (DFA)
- State Machine Design Pattern

---

**Dibuat untuk**: Mata Kuliah Teori Bahasa dan Automata  
**Semester**: 5  
**Tahun**: 2023
