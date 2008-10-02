import FWCore.ParameterSet.Config as cms

process = cms.Process("TESTFIT")


process.load("Geometry.CommonDetUnit.globalTrackingGeometry_cfi")
process.load("TrackingTools.TrackRefitter.globalCosmicMuonTrajectories_cff")
process.load("TrackingTools.TrackRefitter.cosmicMuonTrajectories_cff")
process.load("TrackingTools.TrackRefitter.ctfWithMaterialTrajectoriesP5_cff")

process.load("Configuration.StandardSequences.Services_cff")

process.load("Configuration.StandardSequences.Geometry_cff")

process.load("Configuration.StandardSequences.MagneticField_cff")
process.load("Configuration.GlobalRuns.ForceZeroTeslaField_cff")

process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
process.GlobalTag.globaltag = 'CRZT210_V1::All' 
process.prefer("GlobalTag")


#process.load("Configuration.StandardSequences.Reconstruction_cff")

process.load("RecoLocalTracker.SiPixelRecHits.PixelCPEGeneric_cfi")

process.source = cms.Source("PoolSource",
                            fileNames = cms.untracked.vstring(
    '/store/data/CRUZET4_v1/Cosmics/RECO/CRZT210_V1_SuperPointing_v1/0000/005F51E5-0373-DD11-B6FA-001731AF6B7D.root',
    '/store/data/CRUZET4_v1/Cosmics/RECO/CRZT210_V1_SuperPointing_v1/0000/006F3A6A-0373-DD11-A8E7-00304876A0FF.root',
    '/store/data/CRUZET4_v1/Cosmics/RECO/CRZT210_V1_SuperPointing_v1/0000/02CF5B1E-6476-DD11-A034-003048769E65.root'
    ))

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(100)
)
process.MessageLogger = cms.Service("MessageLogger",
    debugModules = cms.untracked.vstring('*'),
    cout = cms.untracked.PSet(
    #    TrackTransformer = cms.untracked.PSet(
    #        limit = cms.untracked.int32(10000000)
    #    ),
    noLineBreaks = cms.untracked.bool(True),
    #   TracksToTrajectories = cms.untracked.PSet(
    #       limit = cms.untracked.int32(10000000)
    #   ),
        DEBUG = cms.untracked.PSet(
            limit = cms.untracked.int32(0)
        ),
        TrajectoryReader = cms.untracked.PSet(
            limit = cms.untracked.int32(10000000)
        ),
        threshold = cms.untracked.string('DEBUG')
    ),
    categories = cms.untracked.vstring(
    'TrackTransformer', 
    'TracksToTrajectories', 
    'TrajectoryReader'),
    destinations = cms.untracked.vstring('cout')
)

# process.GLBTrajectoriesReader = cms.EDProducer("TrajectoryReader",
#     rootFileName = cms.untracked.string('GLBTajectoriesReader.root'),
#                                              InputLabel = cms.InputTag("globalMuons","Refitted")
# )

# process.STATrajectoriesReader = cms.EDProducer("TrajectoryReader",
#     rootFileName = cms.untracked.string('STATajectoriesReader.root'),
#                                              InputLabel = cms.InputTag("standAloneMuons","Refitted")
# )

process.CTFTrajectoriesReader = cms.EDProducer("TrajectoryReader",
                                               rootFileName = cms.untracked.string('CTFTajectoriesReader.root'),
                                               InputLabel = cms.InputTag("ctfWithMaterialTracksP5","Refitted")
                                               )

#process.glbMuons = cms.Sequence(process.globalMuons*process.GLBTrajectoriesReader)
#process.staMuons = cms.Sequence(process.standAloneMuons*process.STATrajectoriesReader)
process.tk = cms.Sequence(process.ctfWithMaterialTracksP5*process.CTFTrajectoriesReader)

#process.testSTA = cms.Path(process.staMuons+process.tk+process.glbMuons)
#process.testSTA = cms.Path(process.staMuons+process.tk)
process.testSTA = cms.Path(process.tk)

