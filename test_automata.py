import pytest
from automata import LoginAutomata
from auth import login


class TestLoginAutomata:
    """Test untuk class LoginAutomata (DFA Implementation)"""
    
    def test_initial_state(self):
        """Test state awal harus q0"""
        automata = LoginAutomata()
        assert automata.state == "q0"
    
    def test_transition_username_benar(self):
        """Test transisi dari q0 ke q1 dengan username benar"""
        automata = LoginAutomata()
        new_state = automata.transition("username_benar")
        assert new_state == "q1"
        assert automata.state == "q1"
    
    def test_transition_username_salah(self):
        """Test transisi dari q0 ke q2 dengan username salah"""
        automata = LoginAutomata()
        new_state = automata.transition("username_salah")
        assert new_state == "q2"
        assert automata.state == "q2"
    
    def test_transition_password_benar_from_q1(self):
        """Test transisi dari q1 ke q3 (accept state) dengan password benar"""
        automata = LoginAutomata()
        automata.transition("username_benar")  # q0 -> q1
        new_state = automata.transition("password_benar")  # q1 -> q3
        assert new_state == "q3"
        assert automata.state == "q3"
    
    def test_transition_password_salah_from_q1(self):
        """Test transisi dari q1 ke q2 (reject state) dengan password salah"""
        automata = LoginAutomata()
        automata.transition("username_benar")  # q0 -> q1
        new_state = automata.transition("password_salah")  # q1 -> q2
        assert new_state == "q2"
        assert automata.state == "q2"
    
    def test_full_path_to_accept_state(self):
        """Test jalur lengkap menuju accept state (q3)"""
        automata = LoginAutomata()
        automata.transition("username_benar")  # q0 -> q1
        final_state = automata.transition("password_benar")  # q1 -> q3
        assert final_state == "q3"
    
    def test_reject_state_username_salah(self):
        """Test jalur menuju reject state karena username salah"""
        automata = LoginAutomata()
        final_state = automata.transition("username_salah")  # q0 -> q2
        assert final_state == "q2"
    
    def test_reject_state_password_salah(self):
        """Test jalur menuju reject state karena password salah"""
        automata = LoginAutomata()
        automata.transition("username_benar")  # q0 -> q1
        final_state = automata.transition("password_salah")  # q1 -> q2
        assert final_state == "q2"


class TestLoginFunction:
    """Test untuk fungsi login yang menggunakan DFA"""
    
    def test_login_berhasil(self):
        """Test login dengan username dan password benar"""
        result = login("admin", "12345")
        assert result == True
    
    def test_login_username_salah(self):
        """Test login dengan username salah"""
        result = login("user", "12345")
        assert result == False
    
    def test_login_password_salah(self):
        """Test login dengan password salah"""
        result = login("admin", "00000")
        assert result == False
    
    def test_login_username_password_salah(self):
        """Test login dengan username dan password salah"""
        result = login("user", "00000")
        assert result == False
    
    @pytest.mark.parametrize("username,password,expected", [
        ("admin", "12345", True),   # Valid credentials
        ("admin", "wrong", False),  # Wrong password
        ("wrong", "12345", False),  # Wrong username
        ("wrong", "wrong", False),  # Both wrong
        ("", "", False),            # Empty credentials
        ("admin", "", False),       # Empty password
        ("", "12345", False),       # Empty username
    ])
    def test_login_berbagai_input(self, username, password, expected):
        """Test login dengan berbagai kombinasi input"""
        result = login(username, password)
        assert result == expected


class TestDFAProperties:
    """Test properti DFA"""
    
    def test_deterministic_property(self):
        """Test bahwa automata bersifat deterministik (setiap state + input menghasilkan 1 state)"""
        automata = LoginAutomata()
        
        # Dari q0 dengan input yang sama harus selalu ke state yang sama
        automata1 = LoginAutomata()
        automata2 = LoginAutomata()
        
        state1 = automata1.transition("username_benar")
        state2 = automata2.transition("username_benar")
        
        assert state1 == state2 == "q1"
    
    def test_state_persistence(self):
        """Test bahwa state bertahan setelah transisi"""
        automata = LoginAutomata()
        automata.transition("username_benar")
        
        # State harus tetap q1 meskipun tidak ada transisi baru
        assert automata.state == "q1"
        assert automata.state == "q1"  # Check lagi
    
    def test_accept_state_q3(self):
        """Test bahwa q3 adalah accept state"""
        automata = LoginAutomata()
        automata.transition("username_benar")
        automata.transition("password_benar")
        
        # q3 adalah accept state untuk login berhasil
        assert automata.state == "q3"
    
    def test_reject_state_q2(self):
        """Test bahwa q2 adalah reject state"""
        automata = LoginAutomata()
        automata.transition("username_salah")
        
        # q2 adalah reject state
        assert automata.state == "q2"


if __name__ == "__main__":
    pytest.main([__file__, "-v", "--tb=short"])
