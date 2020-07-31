using System.Configuration;

namespace csv_to_db_csharp
{
    public static class helper
    {
        public static string ConnectionVal(string name) {
            return ConfigurationManager.ConnectionStrings[name].ConnectionString;
        }
    }
}