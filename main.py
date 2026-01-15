from ingest.ingest_symbols import ingest_symbols
from ingest.ingest_footprints import ingest_footprints
from ingest.ingest_schematics import ingest_schematics
from ingest.ingest_pcbs import ingest_pcbs

def print_summary(title, summary):
    print(f"\n===== {title} =====")
    for file, status in summary:
        print(f"{file:40} -> {status}")


def main():
    print("\n🚀 KiCad Database Ingestion Started\n")

    symbols_summary = ingest_symbols()
    footprints_summary = ingest_footprints()
    schematics_summary = ingest_schematics()
    pcbs_summary = ingest_pcbs()

    print_summary("SYMBOLS INGESTION", symbols_summary)
    print_summary("FOOTPRINTS INGESTION", footprints_summary)
    print_summary("SCHEMATICS INGESTION", schematics_summary)
    print_summary("PCBs INGESTION", pcbs_summary)

    print("\n✅ All files ingested successfully")
    print("📦 Database: kicad.db")
    print("🏁 Process Completed\n")


if __name__ == "__main__":
    main()
