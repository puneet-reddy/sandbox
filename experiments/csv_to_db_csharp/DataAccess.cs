using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using Dapper;
using System.Data;
using System.Data.SqlClient;


namespace csv_to_db_csharp
{
    public class DataAccess
    {
        public List<ssqa> GetSsqas(int limit) {
            using (IDbConnection conn = new System.Data.SqlClient.SqlConnection(helper.ConnectionVal("AlcatelDB"))) {
                var output = conn.Query<ssqa>($"select top {limit} * from Alcatel.aruba_raw_data.ssqa").ToList();
                return output;
            }
        }
    }
}