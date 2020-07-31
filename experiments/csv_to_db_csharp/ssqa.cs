using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace csv_to_db_csharp
{
    public class ssqa
    {
        public string team { get; set; }
        public ulong emp_id { get; set; }
        public string engineer_name { get; set; }
        public int total_evaluations { get; set; }
        public double soft_skills { get; set; }
        public double language { get; set; }
        public double kci { get; set; }
        public double overall { get; set; }
        public string tenurity { get; set; }

        public string FullInfo {
            get {
                return $"{engineer_name} - {team} - {emp_id} - {overall}";
            }
        }
    }
}