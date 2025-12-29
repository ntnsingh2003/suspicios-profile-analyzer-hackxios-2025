import React, { useState } from 'react';
import './App.css';

// Type definitions matching backend API
interface ProfileData {
  account_age_days: number;
  followers: number;
  following: number;
  post_count: number;
  profile_completed: boolean;
  messages: string[];
}

interface RiskAssessment {
  risk_score: number;
  risk_level: string;
  explanations: string[];
  confidence: number;
  confidence_explanation?: string;
  recommended_actions?: string[];
}

interface DemoData {
  legitimate_profile: ProfileData;
  suspicious_profile: ProfileData;
  romance_scam_profile: ProfileData;
}

const App: React.FC = () => {
  // Form state
  const [profileData, setProfileData] = useState<ProfileData>({
    account_age_days: 365,
    followers: 250,
    following: 180,
    post_count: 120,
    profile_completed: true,
    messages: ['']
  });

  // Analysis results state
  const [assessment, setAssessment] = useState<RiskAssessment | null>(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  // Handle form input changes
  const handleInputChange = (field: keyof ProfileData, value: any) => {
    setProfileData((prev: ProfileData) => ({
      ...prev,
      [field]: value
    }));
  };

  // Handle message changes
  const handleMessageChange = (index: number, value: string) => {
    const newMessages = [...profileData.messages];
    newMessages[index] = value;
    setProfileData((prev: ProfileData) => ({
      ...prev,
      messages: newMessages
    }));
  };

  // Add new message field
  const addMessage = () => {
    setProfileData((prev: ProfileData) => ({
      ...prev,
      messages: [...prev.messages, '']
    }));
  };

  // Remove message field
  const removeMessage = (index: number) => {
    if (profileData.messages.length > 1) {
      const newMessages = profileData.messages.filter((_: string, i: number) => i !== index);
      setProfileData((prev: ProfileData) => ({
        ...prev,
        messages: newMessages
      }));
    }
  };

  // Load demo data
  const loadDemoData = async (type: 'legitimate' | 'suspicious' | 'romance_scam') => {
    try {
      const response = await fetch('http://localhost:8000/demo-data');
      
      if (!response.ok) {
        throw new Error('Failed to fetch demo data');
      }
      
      const demoData: DemoData = await response.json();
      
      let selectedProfile: ProfileData;
      switch (type) {
        case 'legitimate':
          selectedProfile = demoData.legitimate_profile;
          break;
        case 'suspicious':
          selectedProfile = demoData.suspicious_profile;
          break;
        case 'romance_scam':
          selectedProfile = demoData.romance_scam_profile;
          break;
        default:
          throw new Error('Invalid demo type');
      }
      
      // Ensure the profile has all required fields
      const safeProfile: ProfileData = {
        account_age_days: selectedProfile.account_age_days || 0,
        followers: selectedProfile.followers || 0,
        following: selectedProfile.following || 0,
        post_count: selectedProfile.post_count || 0,
        profile_completed: selectedProfile.profile_completed || false,
        messages: selectedProfile.messages || ['']
      };
      
      setProfileData(safeProfile);
      setAssessment(null);
      setError(null);
    } catch (err) {
      console.error('Demo data loading error:', err);
      setError('Failed to load demo data. Please check if the backend server is running.');
    }
  };

  // Submit profile for analysis
  const analyzeProfile = async () => {
    setLoading(true);
    setError(null);
    setAssessment(null);

    try {
      // Filter out empty messages
      const filteredMessages = profileData.messages.filter((msg: string) => msg.trim() !== '');
      
      if (filteredMessages.length === 0) {
        throw new Error('At least one message is required');
      }

      const dataToSend = {
        ...profileData,
        messages: filteredMessages
      };

      const response = await fetch('http://localhost:8000/analyze-profile', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(dataToSend)
      });

      if (!response.ok) {
        const errorData = await response.json().catch(() => ({ detail: 'Server error occurred' }));
        throw new Error(errorData.detail || `Server error: ${response.status}`);
      }

      const result: RiskAssessment = await response.json();
      
      // Ensure all required fields exist with defaults
      const safeResult: RiskAssessment = {
        risk_score: result.risk_score || 0,
        risk_level: result.risk_level || 'Unknown',
        explanations: result.explanations || [],
        confidence: result.confidence || 0,
        confidence_explanation: result.confidence_explanation || 'Assessment reliability information',
        recommended_actions: result.recommended_actions || ['Standard monitoring recommended']
      };
      
      setAssessment(safeResult);
    } catch (err) {
      console.error('Analysis error:', err);
      const errorMessage = err instanceof Error ? err.message : 'An unexpected error occurred';
      setError(`Analysis failed: ${errorMessage}. Please check if the backend server is running on http://localhost:8000`);
    } finally {
      setLoading(false);
    }
  };

  // Get risk level color using industry-standard security colors
  const getRiskColor = (riskLevel: string): string => {
    switch (riskLevel) {
      case 'Minimal Risk':
        return '#28a745'; // Green
      case 'Low Risk':
        return '#6f42c1'; // Purple
      case 'Medium Risk':
        return '#ffc107'; // Yellow/Amber
      case 'High Risk':
        return '#fd7e14'; // Orange
      case 'Critical Risk':
        return '#dc3545'; // Red
      default:
        return '#6c757d'; // Gray
    }
  };

  return (
    <div className="App">
      <header className="App-header">
        <h1>🛡️ Suspicious Profile Analyzer</h1>
        <p>Cybersecurity threat detection with explainable AI for online profile analysis</p>
      </header>

      <main className="main-content">
        <div className="container">
          {/* Demo Data Buttons */}
          <div className="demo-section">
            <h3>Quick Demo</h3>
            <div className="demo-buttons">
              <button 
                onClick={() => loadDemoData('legitimate')}
                className="demo-btn legitimate"
              >
                Load Legitimate Profile
              </button>
              <button 
                onClick={() => loadDemoData('suspicious')}
                className="demo-btn suspicious"
              >
                Load Suspicious Profile
              </button>
              <button 
                onClick={() => loadDemoData('romance_scam')}
                className="demo-btn high-risk"
              >
                Load Romance Scam Profile
              </button>
            </div>
          </div>

          <div className="analysis-container">
            {/* Input Form */}
            <div className="input-section">
              <h2>Profile Data</h2>
              
              <div className="form-group">
                <label>Account Age (days):</label>
                <input
                  type="number"
                  min="0"
                  value={profileData.account_age_days}
                  onChange={(e: React.ChangeEvent<HTMLInputElement>) => handleInputChange('account_age_days', parseInt(e.target.value) || 0)}
                />
              </div>

              <div className="form-row">
                <div className="form-group">
                  <label>Followers:</label>
                  <input
                    type="number"
                    min="0"
                    value={profileData.followers}
                    onChange={(e: React.ChangeEvent<HTMLInputElement>) => handleInputChange('followers', parseInt(e.target.value) || 0)}
                  />
                </div>
                <div className="form-group">
                  <label>Following:</label>
                  <input
                    type="number"
                    min="0"
                    value={profileData.following}
                    onChange={(e: React.ChangeEvent<HTMLInputElement>) => handleInputChange('following', parseInt(e.target.value) || 0)}
                  />
                </div>
              </div>

              <div className="form-group">
                <label>Post Count:</label>
                <input
                  type="number"
                  min="0"
                  value={profileData.post_count}
                  onChange={(e: React.ChangeEvent<HTMLInputElement>) => handleInputChange('post_count', parseInt(e.target.value) || 0)}
                />
              </div>

              <div className="form-group">
                <label>
                  <input
                    type="checkbox"
                    checked={profileData.profile_completed}
                    onChange={(e: React.ChangeEvent<HTMLInputElement>) => handleInputChange('profile_completed', e.target.checked)}
                  />
                  Profile Completed
                </label>
              </div>

              <div className="form-group">
                <label>Messages:</label>
                {profileData.messages.map((message: string, index: number) => (
                  <div key={index} className="message-input">
                    <textarea
                      value={message}
                      onChange={(e: React.ChangeEvent<HTMLTextAreaElement>) => handleMessageChange(index, e.target.value)}
                      placeholder={`Message ${index + 1}...`}
                      rows={2}
                    />
                    {profileData.messages.length > 1 && (
                      <button
                        type="button"
                        onClick={() => removeMessage(index)}
                        className="remove-btn"
                      >
                        ✕
                      </button>
                    )}
                  </div>
                ))}
                <button type="button" onClick={addMessage} className="add-btn">
                  + Add Message
                </button>
              </div>

              <button
                onClick={analyzeProfile}
                disabled={loading}
                className="analyze-btn"
              >
                {loading ? 'Analyzing Security Threats...' : 'Analyze Profile for Threats'}
              </button>
            </div>

            {/* Results Section */}
            <div className="results-section">
              <h2>Security Threat Assessment</h2>
              
              {error && (
                <div className="error">
                  <strong>Error:</strong> {error}
                </div>
              )}

              {assessment && (
                  <div className="assessment-results">
                    <div className="threat-overview">
                      <div className="risk-score">
                        <div 
                          className="score-circle"
                          style={{ borderColor: getRiskColor(assessment.risk_level) }}
                        >
                          <span className="score-number">{assessment.risk_score}</span>
                          <span className="score-label">/ 100</span>
                        </div>
                        <div className="risk-info">
                          <h3 style={{ color: getRiskColor(assessment.risk_level) }}>
                            {assessment.risk_level}
                          </h3>
                          <p>Confidence: {(assessment.confidence * 100).toFixed(0)}%</p>
                          <p className="confidence-explanation">{assessment.confidence_explanation || 'Assessment reliability information'}</p>
                        </div>
                      </div>
                    </div>

                    <div className="threat-indicators">
                      <h4>Security Threat Indicators:</h4>
                      <ul>
                        {(assessment.explanations || []).map((explanation: string, index: number) => (
                          <li key={index}>{explanation}</li>
                        ))}
                      </ul>
                    </div>

                    <div className="security-actions">
                      <h4>Recommended Security Actions:</h4>
                      <ul>
                        {(assessment.recommended_actions || []).map((action: string, index: number) => (
                          <li key={index} className="action-item">{action}</li>
                        ))}
                      </ul>
                    </div>

                    <div className="methodology">
                      <h4>Analysis Methodology:</h4>
                      <p>
                        This threat assessment combines <strong>rule-based detection</strong> (60%) 
                        for known attack patterns with <strong>behavioral analysis</strong> (40%) 
                        for emerging threats. Every security indicator is explained using 
                        established cybersecurity frameworks.
                      </p>
                    </div>
                  </div>
              )}

              {!assessment && !error && !loading && (
                <div className="placeholder">
                  <p>Enter profile data and click "Analyze Profile for Threats" to see security assessment</p>
                </div>
              )}
            </div>
          </div>
        </div>
      </main>

      <footer className="footer">
        <p>
          Cybersecurity threat detection • Structured planning with Kiro • 
          Explainable AI for security operations
        </p>
      </footer>
    </div>
  );
};

export default App;