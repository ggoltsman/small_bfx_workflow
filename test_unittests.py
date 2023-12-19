import sqlite3


class TestSQLQueries:
    db_name = "vcf.db"

    def test_select_pos(self):
        conn = sqlite3.connect(self.db_name)
        cur = conn.cursor()

        cur.execute("SELECT * FROM vcfTable WHERE POS = 17073043")
        res = cur.fetchall()
        assert res[0][1] == 17073043, "Position unit test failed."
        conn.close()

    def test_annot(self):
        conn = sqlite3.connect(self.db_name)
        cur = conn.cursor()

        cur.execute("SELECT * FROM vcfTable WHERE POS = 17073043")
        res = cur.fetchall()
        assert res[0][-1].startswith("ANN="), "Annotation unit test failed."
        conn.close()
