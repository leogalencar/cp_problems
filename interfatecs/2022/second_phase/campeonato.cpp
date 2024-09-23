#include <bits/stdc++.h>

using namespace std;

template<typename A, typename B> ostream& operator<<(ostream &os, const pair<A, B> &p) { return os << '(' << p.first << ", " << p.second << ')'; }
template<typename T_container, typename T = typename enable_if<!is_same<T_container, string>::value, typename T_container::value_type>::type> ostream& operator<<(ostream &os, const T_container &v) { os << '{'; string sep; for (const T &x : v) os << sep << x, sep = ", "; return os << '}'; }
void dbg_out() { cerr << endl; }
template<typename Head, typename... Tail> void dbg_out(Head H, Tail... T) { cerr << ' ' << H; dbg_out(T...); }
#ifdef LOCAL
#define dbg(...) cerr << "(" << #__VA_ARGS__ << "):", dbg_out(__VA_ARGS__)
#else
#define dbg(...)
#endif

#define ar array
#define ll long long
#define ld long double
#define sza(x) ((int)x.size())
#define all(a) (a).begin(), (a).end()

const int MAX_N = 1e5 + 5;
const ll MOD = 1e9 + 7;
const ll INF = 1e9;
const ld EPS = 1e-9;



bool comp(const vector<int>& a, const vector<int>& b) {
    for (size_t i = 0; i < min(a.size(), b.size()); ++i) {
        if (a[i] != b[i]) {
            return a[i] > b[i];
        }
    }

    return a.size() > b.size();
}

void solve() {
    int teamsQty, gamesQty;

    cin >> teamsQty;

    map<int, string> teams;
    vector<vector<int>> stats;
    map<int, int> pos;

    for (int i = 0; i < teamsQty; i++) {
        int id;
        string name;

        cin >> id >> name;

        teams[id] = name;

        pos[id] = i;

        // 0: points, 1: wins, 2: goals_diff, 3: goals, 4: team_id
        stats.push_back({0, 0, 0, 0, id});
    }

    cin >> gamesQty;

    for (int i = 0; i < gamesQty; i++) {
        int t1, t2, p1, p2;

        cin >> t1 >> t2 >> p1 >> p2;

        if (p1 > p2) {
            stats[pos[t1]][0] += 3;
            stats[pos[t1]][1] += 1;
            stats[pos[t1]][2] += (p1 - p2);

            stats[pos[t2]][2] += (p2 - p1);
        } else if (p1 < p2) {
            stats[pos[t2]][0] += 3;
            stats[pos[t2]][1] += 1;
            stats[pos[t2]][2] += (p2 - p1);

            stats[pos[t1]][2] += (p1 - p2);
        } else {
            stats[pos[t1]][0] += 1;
            stats[pos[t2]][0] += 1;
        }

        stats[pos[t1]][3] += p1;
        stats[pos[t2]][3] += p2;
    }

    sort(stats.begin(), stats.end(), comp);

    cout << teams[stats[0][4]] << " CAMPEAO\n";
    cout << teams[stats[1][4]] << " SEGUNDO LUGAR\n";
    cout << teams[stats[2][4]] << " TERCEIRO LUGAR\n";
}

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);
    int tc = 1;
    // cin >> tc;
    for (int t = 1; t <= tc; t++) {
        // cout << "Case #" << t << ": ";
        solve();
    }
}