class Solution {
public:
    vector<int> asteroidCollision(vector<int>& asteroids) {
        stack<int> st;

        for(int i=0; i<asteroids.size(); i++)
        {
            if(st.empty() || asteroids[i] > 0)      // stack empty or asteroid +ve
            {
                st.push(asteroids[i]);              // [4, 3, 2, 1, -10]
            }
            else                            // incoming asteroid -ve
            {
                while(true)
                {
                    int top = st.top();

                    if(top < 0)             // both are -ve (same direction)
                    {
                        st.push(asteroids[i]);
                        break;
                    }
                    else if(top == abs(asteroids[i]))       // both are same size
                    {
                        st.pop();
                        break;
                    }
                    else if(top > abs(asteroids[i]))        // incoming asteroid small
                    {
                        break;
                    }
                    else                                // incoming asteroids large
                    {
                        st.pop();
                        if(st.empty())
                        {
                            st.push(asteroids[i]);
                            break;
                        }
                    }      
                    
                }
            }
        } // end for loop


        vector<int> res(st.size());

        for(int i=st.size()-1; i>=0; i--)
        {
            res[i] = st.top();
            st.pop();
        }

        return res;
    }
};
