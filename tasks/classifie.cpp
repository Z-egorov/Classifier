#include <iostream>
#include <fstream>
#include "classifie.hpp"

int main()
{
    setlocale(LC_ALL, "rus");
    Classifie* c = new Classifie;
    std::filesystem::path p {"test"};
    
    std::vector<std::vector<double>> document_vec;
    std::vector<std::vector<double>> themes_vec;

    std::map<std::string, int> all_docs_task;
    std::stringstream all_docs_texts;
    
    int docs_files_count = 0, themes_files_count = 0;

    for (const auto& theme : std::filesystem::directory_iterator{p/"docs"})
    {
        std::ifstream file(theme.path());
        all_docs_texts << file.rdbuf();
        docs_files_count++;
    }
    
    // std::cout << all_docs_texts.str() << '\n';
    all_docs_task = c -> task_1(all_docs_texts);
    
    std::map<std::string, int> all_themes_task;
    std::stringstream all_themes_texts;
    
    for (const auto& theme : std::filesystem::directory_iterator{p/"themes"})
    {
        std::ifstream file(theme.path());
        all_themes_texts << file.rdbuf();
        themes_files_count++;
    }

    all_themes_task = c -> task_1(all_themes_texts);

// --------------------------------------------------

    // tf_idf (int n, int t, int d, int r)

    // n - общее кол-во слов в документе
    // t - количество вхождений в одном файле
    // r - количетсво документов, где есть слово.
    // d - количество файлов

    for (const auto& theme : std::filesystem::directory_iterator{p/"themes"})
    {
        
        std::ifstream file(theme.path());
        
        std::stringstream ss;
        std::map<std::string, int> m;

        ss << file.rdbuf();
        m = c -> task_1(ss);

        int n = c -> get_words(m);

        int d = themes_files_count;
        std::vector<double> temp_vec;
        for (auto pair_text : m)
        {
            temp_vec.clear();
            int t = c -> get_word_count(m, pair_text.first);
            int r = c -> word_in_themes_count(p, pair_text.first);
            // std::cout << n << ' ' << t << ' ' << d << ' ' << r << '\n';
            double tfedf = c -> tf_idf(n, t, d, r);
            if (tfedf)
                temp_vec.push_back(tfedf);
        }
        themes_vec.push_back(temp_vec);
    }

    int i = 0;
    for (const auto& document : std::filesystem::directory_iterator{p/"docs"})
    {   
        std::ifstream file(document.path());
        std::stringstream ss;
        std::map<std::string, int> m;
        i++;
        ss << file.rdbuf();
        m = c -> task_1(ss);

        int n = c -> get_words(m);
        int d = docs_files_count;
        std::vector<double> temp_vec;
        for (auto pair_text : m)
        {
            int t = c -> get_word_count(m, pair_text.first);
            int r = c -> word_in_docs_count(p, pair_text.first);
            double tfedf = c -> tf_idf(n, t, d, r);
            if (tfedf)
                temp_vec.push_back(tfedf);
        }
        document_vec.push_back(temp_vec);
        std::cout << i << '\n';
    }

    std::ofstream out("classification.txt");
    for (int i = 0; i < document_vec.size(); i++)
    {
        int max = -1;
        int position = 0;

        for (int j = 0; j < themes_vec.size(); j++)
        {   
            auto a = document_vec[i];
            auto b = themes_vec[j];

            double dist = c -> cos_distance(a, b);
            if (max < dist)
            {
                max = dist;
                position = j;
            }
        }
        out << i+1 << ".txt " << position+1 << ".txt\n";
    }

    out.close();
    delete c;
}