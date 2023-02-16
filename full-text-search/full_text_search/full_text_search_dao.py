# Copyright (C) 2023 fem. All rights reserved.
import sqlite3
from ngram import NGram

class Dao:
    def __init__(self):
        db_file = ':memory:'
        self.conn = sqlite3.connect(db_file)
        self.createTextTable()
        self.createMetaTables()
    
    def createTextTable(self):
        cur = self.conn.cursor()
        ddl = 'CREATE VIRTUAL TABLE IF NOT EXISTS TEXT_TABLE USING FTS4 (SOURCE_TYPE TEXT, HASH_SHA1 TEXT, VALUE TEXT, BIGRAM TEXT)'
        cur.execute(ddl)
        self.conn.commit()
        cur.close()
    
    def createMetaTables(self):
        cur = self.conn.cursor()
        ddl1 = 'CREATE TABLE IF NOT EXISTS WWW_TABLE (HASH_SHA1 TEXT, URL TEXT)'
        cur.execute(ddl1)
        
        ddl2 = 'CREATE TABLE IF NOT EXISTS SOURCE_FILE_TABLE (HASH_SHA1 TEXT, FILE_NAME TEXT, LINE_NO INTEGER)'
        cur.execute(ddl2)
        
        ddl3 = 'CREATE TABLE IF NOT EXISTS TEXT_FILE_TABLE (HASH_SHA1 TEXT, FILE_NAME TEXT, LINE_NO INTEGER)'
        cur.execute(ddl3)
        
        ddl4 = 'CREATE TABLE IF NOT EXISTS EXCEL_FILE_TABLE (HASH_SHA1 TEXT, FILE_NAME TEXT, SHEET_NAME TEXT, ROW INTEGER, COL INTEGER)'
        cur.execute(ddl4)
        
        ddl5 = 'CREATE TABLE IF NOT EXISTS WORD_FILE_TABLE (HASH_SHA1 TEXT, FILE_NAME TEXT, PAGE_NO INTEGER)'
        cur.execute(ddl5)
        
        ddl6 = 'CREATE TABLE IF NOT EXISTS PDF_FILE_TABLE (HASH_SHA1 TEXT, FILE_NAME TEXT, PAGE_NO INTEGER)'
        cur.execute(ddl6)
        
        self.conn.commit()
        cur.close()
        
    def isExistTextTable(self, source_type, hash):
        sql = 'SELECT COUNT(*) FROM TEXT_TABLE WHERE SOURCE_TYPE=? AND HASH_SHA1=?'
        cur = self.conn.cursor()
        params = (source_type, hash)
        cur.execute(sql, params)
        data = cur.fetchone()
        cur.close()
        return data[0] > 0
        
    def insertTextTable(self, source_type, hash, text):
        ngram = NGram()
        bigram_text = ngram.getBiGram(text)
        params = (source_type, hash, text, bigram_text)
        sql = 'INSERT INTO TEXT_TABLE VALUES (?,?,?,?)'
        cur = self.conn.cursor()
        cur.execute(sql, params)
        self.conn.commit()
        cur.close()
        
    def insertWwwTable(self, hash, url):
        params = (hash, url)
        sql = 'INSERT INTO WWW_TABLE VALUES (?,?)'
        cur = self.conn.cursor()
        cur.execute(sql, params)
        self.conn.commit()
        cur.close()
    
    def insertSourceFileTable(self, hash, filename, line_no):
        params = (hash, filename, line_no)
        sql = 'INSERT INTO SOURCE_FILE_TABLE VALUES (?,?,?)'
        cur = self.conn.cursor()
        cur.execute(sql, params)
        self.conn.commit()
        cur.close()
        
    def insertTextFileTable(self, hash, filename, line_no):
        params = (hash, filename, line_no)
        sql = 'INSERT INTO TEXT_FILE_TABLE VALUES (?,?,?)'
        cur = self.conn.cursor()
        cur.execute(sql, params)
        self.conn.commit()
        cur.close()
        
    def insertExcelFileTable(self, hash, filename, sheet_name, row, col):
        params = (hash, filename, sheet_name, row, col)
        sql = 'INSERT INTO EXCEL_FILE_TABLE VALUES (?,?,?,?,?)'
        cur = self.conn.cursor()
        cur.execute(sql, params)
        self.conn.commit()
        cur.close()
    
    def insertWordFile(self, hash, filename, page_no):
        params = (hash, filename, page_no)
        sql = 'INSERT INTO WORD_FILE_TABLE VALUES (?,?,?)'
        cur = self.conn.cursor()
        cur.execute(sql, params)
        self.conn.commit()
        cur.close()
    
    def insertPdfFile(self, hash, filename, page_no):
        params = (hash, filename, page_no)
        sql = 'INSERT INTO PDF_FILE_TABLE VALUES (?,?,?)'
        cur = self.conn.cursor()
        cur.execute(sql, params)
        self.conn.commit()
        cur.close()

    def selectTextTable(self, keyword):
        ngram = NGram()
        query_word = ngram.getUniGram(keyword)
        sql = 'SELECT VALUE, SOURCE_TYPE, HASH_SHA1 FROM TEXT_TABLE WHERE BIGRAM MATCH ?'
        cur = self.conn.cursor()
        cur.execute(sql, (query_word,))
        results = cur.fetchall()
        cur.close()
        return results
        
    def selectWwwTable(self, hash):
        sql = 'SELECT URL FROM WWW_TABLE WHERE HASH_SHA1=?'
        cur = self.conn.cursor()
        cur.execute(sql, (hash,))
        result = cur.fetchone()
        cur.close()
        return result
        
    def selectSourceFileTable(self, hash):
        sql = 'SELECT FILE_NAME, LINE_NO FROM SOURCE_FILE_TABLE WHERE HASH_SHA1=?'
        cur = self.conn.cursor()
        cur.execute(sql, (hash,))
        results = cur.fetchall()
        cur.close()
        return results

    def selectTextFileTable(self, hash):
        sql = 'SELECT FILE_NAME, LINE_NO FROM TEXT_FILE_TABLE WHERE HASH_SHA1=?'
        cur = self.conn.cursor()
        cur.execute(sql, (hash,))
        result = cur.fetchall()
        cur.close()
        return result
        
    def selectExcelFileTable(self, hash):
        sql = 'SELECT FILE_NAME, SHEET_NAME, ROW, COL FROM EXCEL_FILE_TABLE WHERE HASH_SHA1=?'
        cur = self.conn.cursor()
        cur.execute(sql, (hash,))
        result = cur.fetchall()
        cur.close()
        return result

    def selectWordFileTable(self, hash):
        sql = 'SELECT FILE_NAME, PAGE_NO FROM WORD_FILE_TABLE WHERE HASH_SHA1=?'
        cur = self.conn.cursor()
        cur.execute(sql, (hash,))
        result = cur.fetchall()
        cur.close()
        return result
        
    def selectPdfFileTable(self, hash):
        sql = 'SELECT FILE_NAME, PAGE_NO FROM PDF_FILE_TABLE WHERE HASH_SHA1=?'
        cur = self.conn.cursor()
        cur.execute(sql, (hash,))
        result = cur.fetchall()
        cur.close()
        return result

