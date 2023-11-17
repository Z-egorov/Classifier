#include <map>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <sstream>
#include <filesystem>


#pragma once

class Classifie
{
    public:

    double tf_idf (int& n, int& t, int& d, int& r)
    {   
        std::string s = "________________________\n";
        double tf = (double(t)/double(n));
        double idf = std::log(double(d)/double(r));

        // std::cout << s << tf << ' ' << idf << '\n' << s;

        return tf*idf;
    }

    double cos_distance (std::vector<double>& v1, std::vector<double>& v2)
    {
        size_t size = std::min(v1.size(), v2.size());
        double dot = 0.0, norm_1 = 0.0, norm_2 = 0.0;
        for (int i = 0; i < size; i++)
        {
            dot += v1[i]*v2[i];
            norm_1 += std::pow(v1[i], 2);
            norm_2 += std::pow(v2[i], 2);
        }

        norm_1 = std::sqrt(norm_1);
        norm_2 = std::sqrt(norm_2);

        double cos_dist = (dot / (norm_1*norm_2));

        return cos_dist;
    }

    std::map<std::string, int> task_1 (std::stringstream& words)
    {
        std::map<std::string, int> result;
        for (std::string word; words >> word; words >> word)
            result[word]++;

        return result;
    }

    int get_word_count (std::map<std::string, int>& m, std::string word)
    {
        return m[word];
    }

    int get_words (std::map<std::string, int>& m)
    {
        int s = 0;
        for (auto c : m)
            s += c.second;

        return s;
    }

    int word_in_docs_count (std::filesystem::path p, std::string word)
    {
        int result = 0;
        for (const auto& theme : std::filesystem::directory_iterator{p/"docs"})
        {
            std::ifstream file(theme.path());
            std::stringstream ss;
            ss << file.rdbuf();
            if (ss.str().find(word))
            {
                result++;
                continue;
            }
        }
        return result;
    }

    int word_in_themes_count (std::filesystem::path p, std::string word)
    {
        int result = 0;
        for (const auto& theme : std::filesystem::directory_iterator{p/"themes"})
        {
            std::ifstream file(theme.path());
            std::stringstream ss;
            ss << file.rdbuf();
            if (ss.str().find(word))
                result++;
        }
        return result;
    }

};