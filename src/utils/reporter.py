import os
import json
from datetime import datetime
from ..core.logger import log

class Reporter:
    def __init__(self, report_name="execution_report"):
        self.report_name = report_name
        self.results = []
        self.start_time = datetime.now()

    def add_result(self, test_name, status, message="", screenshot=None):
        result = {
            "test_name": test_name,
            "status": status,
            "message": message,
            "screenshot": screenshot,
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        self.results.append(result)
        log.info(f"Resultado registrado: {test_name} - {status}")

    def generate_summary(self):
        end_time = datetime.now()
        duration = end_time - self.start_time
        
        summary = {
            "report_name": self.report_name,
            "total_tests": len(self.results),
            "passed": len([r for r in self.results if r['status'] == 'PASS']),
            "failed": len([r for r in self.results if r['status'] == 'FAIL']),
            "duration": str(duration),
            "results": self.results
        }
        
        report_path = os.path.join("reports", f"{self.report_name}_{int(datetime.now().timestamp())}.json")
        if not os.path.exists("reports"):
            os.makedirs("reports")
            
        with open(report_path, "w", encoding="utf-8") as f:
            json.dump(summary, f, indent=4, ensure_ascii=False)
            
        log.info(f"Sumário do relatório gerado em: {report_path}")
        return report_path
