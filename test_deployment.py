#!/usr/bin/env python3
"""
Test script for deployed backend
Usage: python test_deployment.py <backend_url>
Example: python test_deployment.py https://suspicious-profile-analyzer-backend.onrender.com
"""

import sys
import requests
import json

def test_backend(base_url):
    """Test all backend endpoints"""
    print(f"🧪 Testing backend deployment at: {base_url}")
    print("=" * 60)
    
    # Test 1: Health check
    print("1. Testing health check endpoint...")
    try:
        response = requests.get(f"{base_url}/")
        if response.status_code == 200:
            data = response.json()
            print(f"   ✅ Health check passed: {data['message']}")
        else:
            print(f"   ❌ Health check failed: {response.status_code}")
            return False
    except Exception as e:
        print(f"   ❌ Health check error: {e}")
        return False
    
    # Test 2: Demo data endpoint
    print("2. Testing demo data endpoint...")
    try:
        response = requests.get(f"{base_url}/demo-data")
        if response.status_code == 200:
            data = response.json()
            if 'legitimate_profile' in data:
                print("   ✅ Demo data endpoint working")
            else:
                print("   ❌ Demo data missing expected fields")
                return False
        else:
            print(f"   ❌ Demo data failed: {response.status_code}")
            return False
    except Exception as e:
        print(f"   ❌ Demo data error: {e}")
        return False
    
    # Test 3: Profile analysis endpoint
    print("3. Testing profile analysis endpoint...")
    try:
        test_profile = {
            "account_age_days": 7,
            "followers": 2,
            "following": 500,
            "post_count": 50,
            "profile_completed": False,
            "messages": [
                "My darling, I love you so much already.",
                "I am engineer working on oil rig, need emergency money.",
                "Trust me honey, send Western Union transfer immediately."
            ]
        }
        
        response = requests.post(
            f"{base_url}/analyze-profile",
            json=test_profile,
            headers={"Content-Type": "application/json"}
        )
        
        if response.status_code == 200:
            data = response.json()
            if 'risk_score' in data and 'risk_level' in data:
                print(f"   ✅ Analysis working: {data['risk_level']} ({data['risk_score']}/100)")
            else:
                print("   ❌ Analysis response missing expected fields")
                return False
        else:
            print(f"   ❌ Analysis failed: {response.status_code}")
            print(f"   Response: {response.text}")
            return False
    except Exception as e:
        print(f"   ❌ Analysis error: {e}")
        return False
    
    print("=" * 60)
    print("🎉 All tests passed! Backend deployment successful!")
    print(f"📋 API Documentation: {base_url}/docs")
    print(f"🔗 Use this URL for frontend: {base_url}")
    return True

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python test_deployment.py <backend_url>")
        print("Example: python test_deployment.py https://suspicious-profile-analyzer-backend.onrender.com")
        sys.exit(1)
    
    backend_url = sys.argv[1].rstrip('/')
    success = test_backend(backend_url)
    sys.exit(0 if success else 1)