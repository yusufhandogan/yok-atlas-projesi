from atlasdatas.spiders.models import AtlasDB, db_connect, create_table


class ScrapySpiderPipeline(object):

    def __init__(self):
        
        engine = db_connect()
        create_table(engine)

        self.Session = sessionmaker(bind=engine)

    def process_item(self, item, spider):

        session = self.Session()

        atlasdb = AtlasDB()

        atlasdb.PROGRAM_KODU = item["PROGRAM_KODU"]

        atlasdb.PROGRAM_İSMİ = item["PROGRAM_ISMI"]

        atlasdb.BURS_TÜRÜ = item["BURS_TURU"]

        atlasdb.FAKULTE_YUKSEKOKUL = item["FAKULTE_YUKSEKOKUL"]

        atlasdb.PUAN_TURU = item["PUAN_TURU"]

        atlasdb.UNIVERSITE_KODU = item["UNIVERSITE_KODU"]

        atlasdb.UNIVERSITE_TURU = item["UNIVERSITE_TURU"]

        atlasdb.UNIVERSITE_ISMI = item["UNIVERSITE_ISMI"]



        try:
            session.add(atlasdb)
            session.commit()

        except:
            session.rollback()
            raise
    
        finally:
            session.close()

        return item


